# Wortschatz A2

Fiszki do niemieckiego A2: 22 lekcje, 1281 słów z rodzajnikiem, wymową i zdaniami.
Codziennie powtórka i 20 nowych słów, po każdej lekcji sprawdzian (25 pytań, zaliczenie od 80%).

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
