# Typy úloh a ich úrovne

Automaticky vytiahnuté z komentárov generátorov KLARIN. Úroveň 1 je najľahšia; appka podľa výsledkov
dieťaťa volí úroveň sama. Návrh novej úlohy alebo úrovne pošlite cez Issue (pozri CONTRIBUTING.md).

## `write.elements`

write.elements — Čiary a oblúky (grafomotorika pred písaním).
1: zvislé, vodorovné, plná predloha · 2: + šikmé, cik-cak · 3: + vlnovka, girlanda, bodkovaná predloha
4: + arkáda, ovály, meander · 5: + slučky, esá, len štartová bodka · 6: + špirála, v liniatúre

## `draw.trace`

draw.trace — Obťahuj obrázok.
1: kruh, štvorec, plná predloha · 2: + trojuholník · 3: + srdce, domček, bodkovaná · 4: + hviezda, slnko
5: + ryba, oblak · 6: + kvet

## `draw.symmetry`

draw.symmetry — Dokresli druhú polovicu podľa bodiek (zrkadlo je v strede).
1: sieť 5, 3 body · 2: 5, 4 body · 3: 7, 4 body · 4: 7, 5 bodov · 5: 7, 6 bodov · 6: 7, 7 bodov

## `write.small_letters`

write.small_letters — Tlačené malé písmená v štyroch linajkách (poradie ako v 1. ročníku; DE/EN vlastné poradie).
1: prvých 5, plná predloha · 2: do 10 · 3: do 16, bodkovaná · 4: do 24, štartová bodka
5: do 32 (dĺžne a mäkčene), štartová bodka · 6: všetky, bez predlohy

## `write.print_letters`

write.print_letters — Tlačené veľké písmená v poradí 1. ročníka (vlastné predlohy ťahov).
1: A E I Y, plná predloha · 2: + O U T P · 3: + J B K Č, bodkovaná · 4: do N, štartová bodka
5: do Š, štartová bodka v liniatúre · 6: všetky, bez predlohy v liniatúre

## `math.subitize`

math.subitize — „Ukáž 3“: rýchlo uvidieť malý počet bez počítania (kocka).
1: skupina 1–3 → kocka, 2 možnosti · 2: 1–4, 3 možnosti · 3: 1–5
4: číslica 1–5 → kocka (počuje číslo) · 5: číslica 1–6 · 6: číslica 1–10 (rámček s bodkami)

## `math.compare`

math.compare — Kde je viac? Kde je menej?
1: 2 skupiny, rozdiel aspoň 3 (do 6) · 2: rozdiel aspoň 2 · 3: rozdiel 1 (do 8), aj „menej“
4: 3 skupiny do 10 · 5: 3 skupiny, rôzne predmety · 6: väčšie / menšie číslo do 20

## `vocab.colors`

vocab.colors — Nájdi farbu (počuje jej názov).
1: 2 základné · 2: 3 základné · 3: 4 (+ oranžová, fialová) · 4: 4 (+ ružová, hnedá)
5: 5 zo všetkých · 6: 6 zo všetkých, rôzne tvary

## `logic.same`

logic.same — Nájdi rovnaký.
1: obrázok medzi 3 rôznymi · 2: tvar medzi 3 inými tvarmi · 3: 4 tvary, líšia sa tvarom alebo farbou
4: 4 tvary, líšia sa aj veľkosťou · 5: dvojica tvarov, záleží na poradí · 6: trojica tvarov

## `fill.sequence`

fill.sequence — Čo príde ďalej? Rad podľa pravidla, posledné okienko je prázdne.
1: AB AB A? (farby) · 2: AB (tvary) · 3: AAB · 4: ABC · 5: ABB / AABB (tvar aj farba)
6: číselný rad (+1, +2, −1)

## `fill.matrix`

fill.matrix — Doplň okienko. Riadok = tvar, stĺpec = farba (alebo veľkosť).
1–2: 2×2, chýba posledné / ktorékoľvek · 3–4: 3×3 · 5–6: 3×3, riadok = tvar, stĺpec = veľkosť a farba

## `math.add_sub`

math.add_sub — Sčítanie a odčítanie.
1: + do 5 s obrázkami · 2: + a − do 5 s obrázkami · 3: + a − do 10 s obrázkami
4: + a − do 10 číslami · 5: do 20 bez prechodu cez desiatku · 6: do 20 s prechodom cez desiatku

## `math.number_line`

math.number_line — Ktoré číslo chýba?
1: 1–5 · 2: okno 5 čísel do 10 · 3: okno 6 čísel do 20 · 4: dve chýbajúce v okne, pýta sa na prvé
5: odzadu (20 → 0) · 6: po dvoch alebo po desiatkach do 100

## `read.listen`

read.listen — Počúvaj príbeh a odpovedz Áno/Nie (porozumenie počutému).
1–2: krátke príbehy · 3–4: stredné · 5–6: dlhé (Tatry, hrad)

## `logic.odd_category`

logic.odd_category — Čo sem nepatrí? (obrázky z rôznych skupín).

## `logic.odd_shape`

logic.odd_shape — Ktorý je iný? Pravidlo sa s úrovňou stáva abstraktnejším.
1: 3 tvary, rovnaká farba, iný tvar
2: 3 tvary, rovnaký tvar, iná farba
3: 4 tvary, tri rovnaké, štvrtý sa líši tvarom alebo farbou
4: 4 tvary v rôznych farbách, jeden má iný tvar
5: 5 tvarov v rôznych farbách a veľkostiach, jeden má iný tvar
6: 5 rôznych tvarov a farieb, jeden je malý (iná veľkosť)

## `math.count`

math.count — Koľko ich je? Úroveň určuje najväčší počet a počet možností.

## `paths.maze`

paths.maze — Ktorá cesta vedie k domčeku? Cesty sa krížia, dieťa sleduje čiaru očami.
1: 2 cesty, 1 ohyb · 2: 3 cesty, 1 ohyb · 3: 3 cesty, 2 ohyby · 4: 4 cesty, 2 ohyby
5: 4 cesty, 3 ohyby · 6: 5 ciest, 3 ohyby

## `paths.arrows`

paths.arrows — Choď podľa šípok. Kde skončíš? (základ programovania)
1: sieť 3×3, 2 kroky · 2: 3×3, 3 kroky · 3: 4×4, 3 kroky · 4: 4×4, 4 kroky · 5: 5×5, 5 krokov · 6: 5×5, 6 krokov

## `space.prepositions`

space.prepositions — Kde je hviezdička? (na, pod, v, vedľa, nad, za)
1: na / pod · 2: na / pod / v · 3: + vedľa · 4: 4 z (na, pod, v, vedľa, nad) · 5: + za · 6: 4 zo všetkých, nad/na spolu

## `space.left_right`

space.left_right — Vľavo a vpravo (z pohľadu dieťaťa na obrazovku).
1: 2 obrázky, ten vľavo · 2: 2 obrázky, vľavo/vpravo · 3: 3 obrázky, úplne vľavo/vpravo
4: 4 obrázky · 5: čo je vľavo/vpravo od slova · 6: druhý zľava/sprava

## `read.first_sound`

read.first_sound — Na akú hlásku začína slovo? (príručka: „Pomenuj obrázky… ktoré sa začínajú na M“)
SK podľa krokov: 1: M A H I · 2: + J O T · 3: + E B U · 4: + L S · 5: + N P K, malé · 6: ďalšie písmená
DE/EN: celá abeceda, viac možností s úrovňou. Y sa nepýta (znie ako I).

## `read.syllable`

read.syllable — Počuješ slabiku, nájdeš ju napísanú (príručka: „Čítaj slabiky“, diktát MA, MÁ, MO…).
Dĺžne od začiatku (MA – MÁ). 1: M A → MA/MÁ · 2: + H I · 3: + J O T · 4: + E B U L, 4 možnosti
5: + S Y N P K, blízke návnady · 6: ďalšie písmená. Od úrovne 2 veľké aj malé písmená.

## `read.hear`

read.hear — Ktoré slovo / ktorú vetu počuješ? Slová a krátke vety z príručiek a čítacích kartičiek školy,
len z písmen, ktoré dieťa už pozná. Návnady sú podobné (mama – jama – lama), ale znejú inak.
1–3: slová (2, 3, 3 možnosti) · 4–6: vety (2, 3, 3 možnosti). Len SK (texty sú zo slovenskej školy).

## `read.word_picture`

read.word_picture — Prečítaj slovo a nájdi obrázok (bez nahrávky slova, to by prezradilo odpoveď).
SK: len slová z naučených písmen. Obrázkové slová appky sa dajú čítať až po celom 1. diele
(M A H I J O T E B U L S Y N P K) – skôr číta dieťa slová z príručky v úlohe read.hear.
1: 2 obrázky · 2: 3 · 3: + V R · 4: + Z Š D, 4 obrázky · 5: + C Ž Č · 6: všetko, rovnaká skupina

## `read.rhyme`

read.rhyme — „Rýmujú sa tieto slová?“ Appka povie dvojicu, dieťa ťukne Áno/Nie (ide aj bez čítania).
1–2: jednoslabičné · 3–4: dvojslabičné · 5–6: aj podobné, ktoré sa nerýmujú (myška – mačka)

## `read.missing_letter`

read.missing_letter — „Ktoré písmeno chýba?“ Obrázok, slovo s medzerou (KO_ÁČ), výber z 2–4 písmen.
1–2: chýba posledné písmeno, 2 možnosti · 3–4: písmeno v strede, 3 možnosti · 5–6: hocikde, aj s dĺžňom/mäkčeňom, 4 možnosti

## `read.last_sound`

read.last_sound — „Akou hláskou sa slovo končí?“ (Hupsov: posledná hláska slova). SK, DE.
1–2: slová so samohláskou na konci, 2 možnosti · 3–4: všetky, 3 možnosti · 5–6: 4 možnosti

## `read.letter_count`

read.letter_count — „Koľko písmen má slovo?“ (Virgovičová: Koľko písmen mám v mene?). Obrázok a slovo s medzerami.
1–2: do 4 písmen, 2 možnosti · 3–4: do 6, 3 možnosti · 5–6: do 8, 4 možnosti

## `read.true_false`

read.true_false — „Prečítaj vetu. Je to pravda?“ Obrázok a veta, Áno/Nie (Virgovičová: pravda – nepravda,
Hupsov: podčiarkni pravdivú vetu). Veta sa pred odpoveďou nečíta – to je to čítanie.
1–2: iná kategória (pes / jablko) · 3–6: rovnaká kategória (pes / mačka)

## `read.letter_case`

read.letter_case — „Ktoré malé písmeno patrí k veľkému?“ (veľké ↔ malé tlačené písmeno).
1–2: veľké → malé, 2 možnosti · 3–4: 3 možnosti, aj malé → veľké · 5–6: zameniteľné (b d p, m n), aj dĺžne a mäkčene, 4 možnosti

## `fill.routine`

fill.routine — Čo príde potom? Poradie denných činností (rituály večer a ráno).
1–2: dva kroky, vyber ďalší z 2 · 3–4: tri kroky, z 3 · 5–6: chýba krok v strede, z 3

## `sp.akk`

sp.akk — „Ich sehe ___ Bleistift.“ (einen/eine/ein) · „Zeig auf ___ Buch!“ (den/die/das). Len nemčina.
1–2: Ich sehe, školské veci · 3–4: Zeig auf, školské veci · 5–6: oboje, všetky slová

## `read.syllables`

read.syllables — „Koľko slabík počuješ?“ Appka povie slovo, dieťa vytlieska a ťukne na oblúčiky.
1–2: slová s 1–2 slabikami, 2 možnosti · 3–4: do 3 slabík, 3 možnosti · 5–6: do 4 slabík, 4 možnosti

## `sp.article`

sp.article — Der/die/das, ten/tá/to, a/an. Obrázok a slovo bez člena, dieťa vyberie farebný člen.
1: jedlo · 2: + zvieratá · 3: + oblečenie, hračky · 4–6: všetko

## `sp.monster`

sp.monster — Prečítaj (vypočuj) vetu a nájdi monštrum, ktoré o sebe hovorí.
1: 1 veta, 2 monštrá líšiace sa farbou · 2–3: 3 monštrá, farba alebo počet · 4–6: 2 vety

## `sp.verb`

sp.verb — Ktorý tvar slovesa sa hodí? „Er (der Papa) … eine Banane.“
1: ja / ty / on, 2 možnosti · 2: + ona, ono · 3: všetky osoby, 3 možnosti · 4–6: 4 možnosti (EN: max 3)

## `sp.because`

sp.because — Prečo? Dieťa dokončí vetu („…, weil ich durstig bin.“).  1–2: 2 možnosti · 3–6: 3 možnosti

## `read.clap`

read.clap — „Povedz slovo nahlas a pri každej slabike tleskni.“ Dieťa ťuká na dlane, potom Hotovo.
1–2: slová s 1–2 slabikami · 3–4: do 3 · 5–6: do 4

## `read.split`

read.split — „Ako sa slovo delí na slabiky?“ Obrázok, nahrávka slova, možnosti ma-ma / mam-a / m-ama.

## `read.compose`

read.compose — „Počúvaj slabiky. Aké slovo z nich vznikne?“ Appka povie ma – ma, dieťa ťukne na obrázok.
1–2: 2 obrázky · 3–4: 3 · 5–6: 4, návnady začínajú rovnakou slabikou, ak sa dá

## `read.build`

read.build — „Poskladaj slovo. Ťukaj na písmená po poradí.“ Obrázok, nahrávka slova, rozhádzané písmená.
1–2: 3 písmená · 3–4: do 5 písmen, +1 navyše · 5–6: do 7 písmen, +2 navyše

## `vocab.find_word`

vocab.find_word — Počuješ slovo, nájdeš obrázok.
1–3: 2/3/4 obrázky z rôznych skupín · 4–6: 4/6/6 obrázkov z jednej skupiny (ťažšie rozlíšiť)
