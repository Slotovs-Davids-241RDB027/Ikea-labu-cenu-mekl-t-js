# Ikea-labu-cenu-meketajs

Šī Python programma palīdz lietotājiem atrast produktus IKEA "Pēdējās iespējas" sadaļā, kuru cena atbilst norādītajiem kritērijiem — maksimālā un minimālā cena, kā arī atslēgvārdi produktu aprakstos. Programma veic web scraping uz IKEA mājaslapu un atgriež produktus, kuru cena ir norādītajā diapazonā un kas atbilst meklētajiem vārdiem.

## Funkcionalitāte

* Maksimālā cena: Lietotājs ievada maksimālo cenu, un programma atrod visus produktus ar cenu līdz norādītajai vērtībai.

* Minimālā cena: Ja nepieciešams, var norādīt minimālo cenu, lai filtrētu produktus, kas ir augstāki par šo cenu.

* Atslēgvārdi: Lietotājs var ievadīt vairākus atslēgvārdus, kurus programma meklēs produktu aprakstos.

## Bibliotēkas

Projekta izstrādē tiek izmantotas šādas Python bibliotēkas:

- **requests** – Lai veiktu HTTP pieprasījumus un iegūtu tīmekļa lapas saturu.
- **beautifulsoup4** – Lai parsētu HTML lapas saturu un iegūtu nepieciešamo informāciju par produktiem.

## Programmas darbība

Kā izmantot šo programmu:
1) Instalē Python.
2) Instalē nepieciešamās bibliotēkas ar komandu:
   pip install requests beautifulsoup4
3) Palaid programmu:
Atver main.py failu Python vidē.
Ievadi nepieciešamos parametrus: maksimālo cenu, minimālo cenu un/vai atslēgvārdus aprakstā.
**Programma atgriezīs:
**Produkta nosaukumu**
**Produkta aprakstu**
**Cenu**
**Saite uz produktu IKEA mājaslapā**

## Koda Apraksts
Šis ir programmas kods, kas veic tīmekļa datu ieguvi no IKEA lapas un atgriež rezultātus, kas atbilst lietotāja norādītajai cenai. Kodā tiek izmantotas divas galvenās bibliotēkas: requests un beautifulsoup4, lai veiktu HTTP pieprasījumus un analizētu iegūtos HTML datus.

Galvenās funkcijas un to apraksts:

1) **iegut_preces_filtrsetas(max_cena, min_cena=None, atslegvardu_saraksts=None)**
Šī funkcija ir galvenā, kas iegūst datus no IKEA "Pēdējās iespējas" sadaļas un filtrē produktus pēc lietotāja norādītajiem kritērijiem: maksimālās cenas, minimālās cenas un atslēgvārdiem.
Ievadparametri:
max_cena: Maksimālā cena (skaitlis, EUR).
min_cena: Minimālā cena (skaitlis, EUR) (neobligāts).
atslegvardu_saraksts: Saraksts ar atslēgvārdiem, kas jāmeklē produktu aprakstos (neobligāts).
Izvades rezultāts:
Saraksts ar produktiem, kas atbilst lietotāja kritērijiem (nosaukums, cena, apraksts, saite uz produktu).

2) **extract_price(cena_info)**
Šī funkcija ir atbildīga par cenas izvilkšanu no HTML elementa, kas satur cenu. Tā pārbauda vairākus HTML atribūtus, lai atrastu vispiemērotāko cenu, jo IKEA lapā cenas var būt dažādās struktūrās.
Ievadparametri:
cena_info: HTML elements, kas satur produkta cenu.
Izvades rezultāts:
Atgriež cenas vērtību kā skaitli (float).

3) **saite_uz_produktu(prece)**
Šī funkcija iegūst saiti uz katru produktu IKEA mājaslapā. Ja saite ir relatīva (ne pilnīga URL), tiek pievienota pamatadrese, lai iegūtu pilnu saiti uz produktu.
Ievadparametri:
prece: HTML elements, kas pārstāv produktu.
Izvades rezultāts:
Pilna URL saite uz produktu.

4) **filtrēt_atbilstošos_produktus(bloka, max_cena, min_cena, atslegvardu_saraksts)**
Šī funkcija veic produktu filtrēšanu pēc cenas un atslēgvārdiem. Tā pārbauda katru produktu, lai noskaidrotu, vai tas atbilst lietotāja norādītajiem kritērijiem, un atgriež sarakstu ar atbilstošajiem produktiem.
Ievadparametri:
bloka: Saraksts ar visiem produktiem, kas iegūti no lapas.
max_cena: Maksimālā cena.
min_cena: Minimālā cena.
atslegvardu_saraksts: Atslēgvārdi, kas jāmeklē produktu aprakstos.
Izvades rezultāts:
Saraksts ar produktiem, kas atbilst visiem kritērijiem (nosaukums, cena, apraksts, saite).

5) **print_atrodot_produktus(atrastas_preces)**
Šī funkcija ir atbildīga par atrasto produktu izdrukāšanu, ja ir atrasti atbilstoši rezultāti. Tā izvada produktu nosaukumus, cenas, aprakstus un saites uz attiecīgajiem produktiem.
Ievadparametri:
atrastas_preces: Saraksts ar atbilstošiem produktiem.
Izvades rezultāts:
Produktu saraksts tiek izdrukāts komandrindā.

## Programmas Prasības
Python 3.x vai jaunāka versija

Interneta pieslēgums, lai varētu veikt pieprasījumus uz IKEA mājaslapu

Saite uz video ierakstu: https://drive.google.com/file/d/1ZvsRym41xscxWLyQj_viGU8gJC-aL1fL/view?usp=sharing
