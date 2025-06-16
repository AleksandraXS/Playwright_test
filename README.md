# Cookie managment

## Link 
- code repo - https://github.com/AleksandraXS/Playwright_test

## Pobranie pliku README.md
- należy pobrać tekst README.md z repozytorium w wersji raw.
- w projekcie (w miejscu gdzie znajduje się test Test.py) należy utworzyć plik
  1. New -> File
  2. Nazwać -> README.md
  3. wkleić dane skopiowane z pliku znajdującego się w repozytorium (RAW)
  4. Po wykonaniu należy przejść dalej.

### 1. Aby testy zadziałały nalezy:
1. należy pobrać z GitHub repozytorium
2. nastepnie utworzyć środowisko wirtualne dla pythona
3. kolejnym krokiem będzie wpisanie w terminal (instalacja) playwright
     - pip install playwright
     - playwright install (instalacja wszytskich przeglądarek)

### 2. Test uruchamiamy za pomocą skrótu klawiszowego Shift+F10 lub klasycznie z przycisku u góry.

### 3. Wykonanie testu

- Test wykona dwa screenshoty, które potwierdzają wejście w poszczególne sekcje 
- dostosuj
- wybranie cookies analitycznych (pierwsze założenie testu)

Dodatkowo, test wykona ruch na stronie, a żeby zobaczyć faktyczne wykorzystanie cookie analitycznych, które również jest częścią testu, sprawdzane jest oraz wyprintowane jakiecookies zostały użyte. ~~ można byłoby na inny sposób sprawdzić użycie i sprawdzenie, poprzez ponowne wejście w Ustawienia cookies na stronie lub bezpośrednio pzrez ustawienia przegladarki, ale taki sposób wydawał mi się najbardziej trafiony :)