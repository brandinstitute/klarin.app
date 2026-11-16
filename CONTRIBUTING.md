# Ako prispieť / ako pridať úlohu

Ďakujeme! Každá zmena prejde kontrolou (pedagogicky aj technicky), kým sa dostane do appky.

## Najjednoduchšie: Issue
Otvorte **Issue** a napíšte:
1. **Ktorá zručnosť** (napr. `read.rhyme`, pozri `docs/ULOHY.md`) alebo „nová úloha“.
2. **Pre koho** – vek alebo ročník, jazyk (SK / DE / EN).
3. **Čo má dieťa robiť** a čo je správna odpoveď – 2–3 príklady.
4. **Čo je ľahšie a čo ťažšie** – ako by sa úloha stupňovala (úroveň 1 → 6, prípadne 7–9).

## Oprava textu alebo slova
- Texty, ktoré appka číta, sú v `obsah/texty/<jazyk>.json` (kľúč → text). Opravte text, kľúč nemeňte.
- Slová sú v `obsah/slovna_zasoba.json`. Nové slovo potrebuje preklad do všetkých troch jazykov a obrázok
  (obrázky dodávame my – stačí napísať, čo má byť na obrázku).
- Pošlite **Pull Request** s krátkym popisom prečo.

## Zásady obsahu
- Úlohy majú dieťa **naučiť, nie nachytať**: všetko potrebné je v zadaní, žiadne chytáky.
- **Žiadne časové odpočítavanie**, žiadne reklamy, žiadne nákupy.
- Nič neprepisujte z učebníc, pracovných zošitov ani cudzích webov (autorské práva) – len vlastné nápady.
- Žiadne skutočné mená detí ani osobné údaje.
- Slovenčina a nemčina musia byť gramaticky správne – ak si nie ste istí, napíšte to do popisu.

## Šablóny písma
`sablony_pisma.json`: každý ťah je zoznam bodov `[x, y]` v smere písania, súradnice 0–1, `y` rastie nadol.
Poradie ťahov a smer sú dôležité – appka podľa nich kontroluje, či dieťa píše správne.

Prispievaním súhlasíte so zverejnením vášho príspevku pod licenciou CC BY-SA 4.0.
