"""Kontrola obsahu KLARIN pred zlúčením zmeny (spúšťa sa aj automaticky pri každom Pull Requeste).

Použitie:  python nastroje/kontrola.py
Kontroluje: platný JSON, texty vo všetkých troch jazykoch s rovnakými kľúčmi a zástupnými znakmi {x},
slovnú zásobu (preklady, člen v nemčine, jedinečné kódy) a zručnosti (ostrov, názvy, úrovne, nadväznosť).
Check: valid JSON, texts in all three languages with matching keys and {placeholders},
vocabulary (translations, German article, unique codes) and skills (island, titles, levels, prerequisites).
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LANGS = ('sk', 'de', 'en')
errors = []


def err(where, msg):
    errors.append(f'{where}: {msg}')


def load(rel):
    p = os.path.join(ROOT, rel)
    try:
        with open(p, encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        err(rel, 'súbor chýba / file missing')
    except json.JSONDecodeError as e:
        err(rel, f'neplatný JSON / invalid JSON – riadok {e.lineno}, stĺpec {e.colno}: {e.msg}')
    return None


def placeholders(text):
    return sorted(set(re.findall(r'\{(\w+)\}', text)))


# ---------------- texty ----------------
texts = {l: load(f'obsah/texty/{l}.json') for l in LANGS}
if all(isinstance(t, dict) for t in texts.values()):
    keys = {l: set(t) for l, t in texts.items()}
    for l in LANGS:
        for other in LANGS:
            for k in sorted(keys[other] - keys[l]):
                err(f'obsah/texty/{l}.json', f'chýba kľúč / missing key "{k}" (je v {other}.json)')
    for k in sorted(keys['sk'] & keys['de'] & keys['en']):
        vals = {l: texts[l][k] for l in LANGS}
        for l, v in vals.items():
            if not isinstance(v, str) or not v.strip():
                err(f'obsah/texty/{l}.json', f'"{k}" je prázdny / empty')
        ph = {l: placeholders(v) for l, v in vals.items() if isinstance(v, str)}
        if len({tuple(p) for p in ph.values()}) > 1:
            err('obsah/texty', f'"{k}" má rôzne zástupné znaky / placeholders differ: {ph}')

# ---------------- slovná zásoba ----------------
vocab = load('obsah/slovna_zasoba.json')
if isinstance(vocab, dict):
    seen = set()
    for i, w in enumerate(vocab.get('words', [])):
        where = f'obsah/slovna_zasoba.json words[{i}]'
        code = w.get('code')
        if not code or not re.fullmatch(r'[a-z0-9_]+', code):
            err(where, f'kód musí byť malými písmenami bez medzier / code must be lowercase: {code!r}')
        if code in seen:
            err(where, f'kód "{code}" je dvakrát / duplicate code')
        seen.add(code)
        for l in LANGS:
            if not str(w.get(l, '')).strip():
                err(where, f'"{code}": chýba preklad / missing translation "{l}"')
        if w.get('de_article') not in ('der', 'die', 'das', None):
            err(where, f'"{code}": de_article musí byť der/die/das')
        if not isinstance(w.get('level'), int) or not 1 <= w['level'] <= 9:
            err(where, f'"{code}": level musí byť číslo 1–9')

# ---------------- zručnosti ----------------
skills = load('obsah/zrucnosti.json')
if isinstance(skills, dict):
    islands = skills.get('islands', {})
    island_codes = set(islands) if isinstance(islands, dict) else {i[0] for i in islands}
    codes = [s.get('code') for s in skills.get('skills', [])]
    for i, s in enumerate(skills.get('skills', [])):
        where = f'obsah/zrucnosti.json skills[{i}] {s.get("code")}'
        if codes.count(s.get('code')) > 1:
            err(where, 'kód je dvakrát / duplicate code')
        if s.get('island') not in island_codes:
            err(where, f'neznámy ostrov / unknown island "{s.get("island")}"')
        for l in LANGS:
            if not str(s.get('title', {}).get(l, '')).strip():
                err(where, f'chýba názov / missing title "{l}"')
        lo, hi = s.get('min_level', 1), s.get('max_level', 1)
        if not (isinstance(lo, int) and isinstance(hi, int) and 1 <= lo <= hi <= 9):
            err(where, f'úrovne musia byť 1 ≤ min_level ≤ max_level ≤ 9 (je {lo}–{hi})')
        for r in s.get('requires', []):
            if r not in codes:
                err(where, f'nadväzuje na neexistujúcu zručnosť / requires unknown "{r}"')

# ---------------- šablóny písma ----------------
tpl = load('sablony_pisma.json')
if isinstance(tpl, dict):
    def check_strokes(name, strokes):
        for si, stroke in enumerate(strokes or []):
            pts = stroke if isinstance(stroke, list) else stroke.get('points', []) if isinstance(stroke, dict) else []
            for pt in pts:
                if not (isinstance(pt, list) and len(pt) == 2 and all(isinstance(c, (int, float)) and -0.5 <= c <= 1.5 for c in pt)):
                    err('sablony_pisma.json', f'{name} ťah {si + 1}: bod {pt!r} nie je [x, y] v rozsahu 0–1')
                    return

    for group in ('elements', 'pictures', 'print_capitals'):
        items = tpl.get(group, [])
        pairs = items.items() if isinstance(items, dict) else [(it.get('code', i) if isinstance(it, dict) else i, it) for i, it in enumerate(items)]
        for name, item in pairs:
            strokes = item.get('strokes') if isinstance(item, dict) else item
            if isinstance(strokes, list):
                check_strokes(f'{group} {name}', strokes)
            else:
                err('sablony_pisma.json', f'{group} {name}: chýbajú ťahy / missing strokes')

if errors:
    print(f'Našli sa chyby ({len(errors)}) / {len(errors)} problem(s) found:\n')
    print('\n'.join(f'  - {e}' for e in errors))
    sys.exit(1)
print('Obsah je v poriadku. / Content OK.')
