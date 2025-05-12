# Ikea-labu-cenu-meketajs

Šis projekts ir Python programma, kas palīdz lietotājiem atrast produktus IKEA "Pēdējās iespējas" sadaļā, kuru cena nepārsniedz norādīto maksimālo cenu. Lietotājs ievada vēlamo maksimālo cenu, un programma automātiski meklē visus produktus, kuru cena ir mazāka vai vienāda ar šo vērtību, un atgriež šo produktu nosaukumus, aprakstus, cenas un saites uz produktiem.
Šī programma izmanto **web scraping** tehniku, lai iegūtu datus no IKEA mājaslapas un izfiltrētu tos atbilstoši lietotāja norādītajam cenu limitam.

## Tehnoloģijas un bibliotēkas

Projekta izstrādē tiek izmantotas šādas Python bibliotēkas:

- **requests** – Lai veiktu HTTP pieprasījumus un iegūtu tīmekļa lapas saturu.
- **beautifulsoup4** – Lai parsētu HTML lapas saturu un iegūtu nepieciešamo informāciju par produktiem.

## Programmas darbība

Kā izmantot šo programmu:
1) Instalē Python (ja vēl nav instalēts).
2) Instalē nepieciešamās bibliotēkas ar komandu:
   pip install requests beautifulsoup4
3) Palaid programmu:
Atver Python failu un palaid to.
Ievadi vēlamo maksimālo cenu (EUR) kā skaitli.
4)Programma atgriezīs:
Produktu nosaukumus.
Produktu aprakstus.
Cenas.
Saites uz konkrētiem produktiem IKEA mājaslapā.

## Koda Apraksts
iegut_preces_lidz_cenai(max_cena) – Funkcija, kas iegūst datus no IKEA tīmekļa lapas, parsē HTML un atgriež tos produktus, kuru cena ir mazāka vai vienāda ar lietotāja ievadīto cenu.

Saites apstrāde – Programma izvelk katram produktam saiti uz attiecīgo produktu.

Cena un apraksts – Tiek iegūti arī cenu un apraksta dati par katru produktu, un tie tiek atspoguļoti lietotājam.

## Programmas Prasības
Python 3.x vai jaunāka versija

Interneta pieslēgums, lai varētu veikt pieprasījumus uz IKEA mājaslapu
