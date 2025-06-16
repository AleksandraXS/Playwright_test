Cookie managment

Aby testy zadziałały - należy pobrać z GitHub repozytorium oraz zaistalować potrzebne dane (pip install playwright, playwright install) i oczywiście mieć pobranego python'a.

Test uruchamiamy za pomocą skrótu klawiszowego Shift+F10 lub klasycznie z przycisku u góry.

Test wykona dwa screenshoty, które potwierdzają wejście w poszczególne sekcje -> dostosuj, a następnie wybranie cookies analitycznych (pierwsze założenie testu)

Dodatkowo, test wykona ruch na stronie, a żeby zobaczyć faktyczne wykorzystanie cookie analitycznych, które również jest częścią testu, sprawdzane jest oraz wyprintowane jakiecookies zostały użyte. ~~ można byłoby na inny sposób sprawdzić użycie i sprawdzenie, poprzez ponowne wejście w Ustawienia cookies na stronie lub bezpośrednio pzrez ustawienia przegladarki, ale taki sposób wydawał mi się najbardziej trafiony :)
