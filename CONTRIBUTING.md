# Ako prispieť do KLARIN

*Deutsch und English: [unten](#deutsch).*

Ďakujeme, že chcete pomôcť! Tento návod vás prevedie od nápadu až po zmenu v appke. Programovať nemusíte.

## 1. Najjednoduchšie: napíšte nám (Issue)

Kliknite na **Issues → New issue** a vyberte formulár:

| Formulár | Kedy ho použiť |
|---|---|
| **Nová úloha alebo úroveň** | máte nápad na novú aktivitu alebo na lepšie stupňovanie náročnosti |
| **Chyba v obsahu** | zadanie je nejasné, odpoveď nesedí, obrázok nezodpovedá slovu |
| **Preklad** | nemčina alebo angličtina neznie prirodzene, prípadne je chybná |
| **Nové slovo** | chcete doplniť slovo do slovnej zásoby (s prekladom do troch jazykov) |

Formulár sa vás opýta na všetko potrebné. Na Issue sa vám ozveme, zvyčajne do týždňa.

## 2. Oprava priamo v súbore (Pull Request v prehliadači)

Na malé opravy textu netreba nič inštalovať:

1. Otvorte súbor, napríklad `obsah/texty/sk.json`.
2. Kliknite na ikonu ceruzky (**Edit this file**). GitHub si vytvorí vašu kópiu (fork).
3. Opravte **text za dvojbodkou**. Kľúč pred dvojbodkou (napr. `"count.prompt"`) nemeňte.
   Zástupné znaky v zložených zátvorkách, napr. `{n}`, musia ostať vo všetkých jazykoch rovnaké.
4. Dole napíšte krátky popis (čo a prečo) a kliknite na **Propose changes → Create pull request**.
5. Automatická kontrola (`nastroje/kontrola.py`) do pár minút ukáže zelenú fajku alebo presne napíše, čo opraviť.

### Väčšie zmeny na vlastnom počítači
```bash
git clone https://github.com/<vas-ucet>/klarin.app.git
cd klarin.app
python nastroje/kontrola.py      # Python 3.9+, nič ďalšie netreba
```
Potom zmeny pošlite cez Pull Request ako zvyčajne.

## 3. Čo je kde

| Súbor | Ako vyzerá záznam |
|---|---|
| `obsah/texty/<jazyk>.json` | `"kľúč": "text, ktorý appka číta nahlas"`, rovnaké kľúče vo všetkých troch jazykoch |
| `obsah/slovna_zasoba.json` | `{"code": "apple", "sk": "jablko", "de": "Apfel", "de_article": "der", "en": "apple", "category": "fruit", "level": 1}` |
| `obsah/zrucnosti.json` | zručnosť s kódom (napr. `math.count`), ostrovom, úrovňami `min_level`–`max_level` a popisom každej úrovne |
| `sablony_pisma.json` | každý ťah je zoznam bodov `[x, y]` v smere písania, súradnice 0–1, `y` rastie nadol |
| `docs/ULOHY.md` | čitateľný popis všetkých typov úloh (generuje sa automaticky) |

**Úrovne:** 1 je najľahšia. Appka podľa výsledkov dieťaťa volí úroveň sama, preto má zmysel
navrhovať aj „medzistupne“, keď je skok medzi úrovňami priveľký.

**Obrázky slov** dodávame my. Pri novom slove stačí napísať, čo má byť na obrázku.

## 4. Zásady obsahu

- **Naučiť, nie nachytať:** všetko potrebné je v zadaní, žiadne chytáky ani podfuky.
- **Bez tlaku:** žiadne odpočítavanie času, súťaženie s inými deťmi, reklamy ani nákupy.
- **Krátko a nahlas:** zadanie sa číta nahlas, dieťa nemusí vedieť čítať. Najviac jedna krátka veta.
- **Vlastná tvorba:** nič neprepisujte z učebníc, pracovných zošitov ani cudzích webov (autorské práva).
- **Súkromie:** žiadne skutočné mená detí, fotky ani iné osobné údaje.
- **Jazyk:** slovenčina a nemčina musia byť gramaticky správne. Ak si nie ste istí, napíšte to do popisu,
  radi pomôžeme.
- **Pre všetky deti:** myslite na deti, ktoré ešte nečítajú, ľavákov, deti s inou materčinou a na rôzne
  rodiny a prostredia.

## 5. Čo sa deje po odoslaní

1. Automatická kontrola obsahu.
2. Pedagogická a jazyková kontrola (správca repozitára, pri nemčine a angličtine aj rodený hovoriaci).
3. Zlúčenie a zaradenie do najbližšej verzie appky.
4. Prispievateľov uvádzame v poďakovaní (môžete požiadať, aby sme vaše meno neuvádzali).

Prispievaním súhlasíte so zverejnením príspevku pod licenciou [CC BY-SA 4.0](LICENSE.md)
a s pravidlami [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

---

## Deutsch

1. **Einfachster Weg:** *Issues → New issue* und ein Formular wählen (neue Aufgabe, Fehler im Inhalt,
   Übersetzung, neues Wort). Vorschläge auf Deutsch sind willkommen.
2. **Direkt im Browser ändern:** Datei öffnen (z. B. `obsah/texty/de.json`), auf den Stift klicken,
   **nur den Text nach dem Doppelpunkt** ändern (Schlüssel und Platzhalter wie `{n}` bleiben gleich),
   *Propose changes → Create pull request*.
3. Eine automatische Prüfung (`nastroje/kontrola.py`) zeigt in wenigen Minuten, ob alles passt.
4. Grundsätze: Aufgaben sollen lehren, nicht hereinlegen; kein Zeitdruck, keine Werbung, keine Käufe;
   nichts aus Schulbüchern abschreiben; keine echten Namen von Kindern.

Mit Ihrem Beitrag stimmen Sie der Veröffentlichung unter [CC BY-SA 4.0](LICENSE.md) zu.

## English

1. **Easiest:** *Issues → New issue* and pick a form (new task, content issue, translation, new word).
   Issues in English are welcome.
2. **Edit in the browser:** open a file (e.g. `obsah/texty/en.json`), click the pencil, change **only the
   text after the colon** (keep keys and placeholders such as `{n}`), then *Propose changes → Create pull request*.
3. An automatic check (`nastroje/kontrola.py`) tells you within minutes whether everything is fine.
4. Principles: tasks should teach, not trick; no timers, ads or purchases; nothing copied from textbooks;
   no real children's names.

By contributing you agree to publish your contribution under [CC BY-SA 4.0](LICENSE.md).
