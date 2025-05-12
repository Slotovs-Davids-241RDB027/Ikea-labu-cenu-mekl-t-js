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
Šis ir programmas kods, kas veic tīmekļa datu ieguvi no IKEA lapas un atgriež rezultātus, kas atbilst lietotāja norādītajai cenai. Kodā tiek izmantotas divas galvenās bibliotēkas: requests un beautifulsoup4, lai veiktu HTTP pieprasījumus un analizētu iegūtos HTML datus.

Galvenās funkcijas un to apraksts:
1) **iegut_preces_lidz_cenai(max_cena)**
Šī funkcija atbild par galveno darbību – datu iegūšanu no IKEA lapas un rezultātu filtrēšanu pēc lietotāja ievadītās maksimālās cenas.

2) **extract_price(cena_info)**
Šī funkcija ir atbildīga par cenas izvilkšanu no HTML elementa, kas satur cenu. IKEA lapā cenas var būt dažādās struktūrās, tādēļ šī funkcija mēģina atrast vispiemērotāko cenu, pārbaudot vairākus HTML atribūtus.

3) **saite uz produktu**
Katram produktam tiek atrasta saite, kas novirza uz konkrēto produktu IKEA mājaslapā. Programma izmanto prece.find("a", class_="productLink")["href"], lai iegūtu pilnu URL, kur lietotājs var iegādāties vai aplūkot papildus informāciju par produktu.

## Programmas Prasības
Python 3.x vai jaunāka versija

Interneta pieslēgums, lai varētu veikt pieprasījumus uz IKEA mājaslapu

Saite uz video ierakstu: https://drive.google.com/file/d/12xXm-8w5yjGFY1jwIcQSzkCS4sAKpQI_/view?usp=sharing
