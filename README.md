# Wortschatz A2

Fiszki do niemieckiego A2: 22 lekcje, 1281 słów z rodzajnikiem, wymową i zdaniami.
Każda lekcja dzieli się na części po ok. 20 słów: najpierw poznajesz słowa, potem fiszki (jak w Quizlecie: stuknij = odwróć, w prawo = umiem, w lewo = jeszcze nie, DE → PL albo PL → DE). Po wszystkich częściach sprawdzian (25 pytań, zaliczenie od 80%). Powtórki według cyklu 1/3/7/14/30/60 dni. Tempo ustalasz sam.

Działa jako aplikacja na iPhonie: otwórz stronę w Safari → Udostępnij → „Do ekranu początkowego”.
Działa offline, a postęp zapisuje się na urządzeniu.

## Struktura

| Ścieżka | Co to jest |
|---|---|
| `index.html`, `sw.js` | zbudowana aplikacja (nie edytować ręcznie) |
| `manifest.webmanifest`, `*.png` | ikony i ustawienia instalacji |
| `src/app.html` | interfejs i logika |
| `src/data1.js`–`src/data4.js` | słownictwo i teksty lekcji |
| `src/fonts/` | czcionki Barlow (osadzane w index.html, żeby działało offline) |
| `src/build.py` | składa `index.html` i `sw.js` |

## Jak wprowadzić zmianę

1. Edytuj pliki w `src/`.
2. `python src/build.py`
3. Commit i push. GitHub Pages opublikuje nową wersję, a telefon pobierze ją przy następnym uruchomieniu z internetem.
