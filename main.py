import requests
from bs4 import BeautifulSoup

def iegut_preces_filtrsetas(max_cena, min_cena=None, atslegvardu_saraksts=None):
    url = "https://www.ikea.lv/lv/last-chance"
    atbilde = requests.get(url)

    if atbilde.status_code != 200:
        print("Neizdevās ielādēt lapu")
        return

    soup = BeautifulSoup(atbilde.content, "html.parser")
    bloki = soup.find_all(class_="itemBlock")

    atrastie = []

    for bloks in bloki:
        nosaukums_elem = bloks.find("h3")
        apraksts_elem = bloks.find("h4", class_="itemFacts")
        cena_elem = bloks.find("span", {"data-price": True})
        saite_elem = bloks.find("a", href=True)

        if nosaukums_elem and cena_elem and saite_elem:
            try:
                cena = float(cena_elem["data-price"])
                if (min_cena is not None and cena < min_cena) or cena > max_cena:
                    continue

                apraksts = apraksts_elem.get_text(strip=True).lower() if apraksts_elem else ""

                if atslegvardu_saraksts:
                    if not any(vards in apraksts for vards in atslegvardu_saraksts):
                        continue

                saite = saite_elem["href"]
                if not saite.startswith("http"):
                    saite = "https://www.ikea.lv" + saite

                atrastie.append({
                    "nosaukums": nosaukums_elem.get_text(strip=True),
                    "apraksts": apraksts_elem.get_text(strip=True) if apraksts_elem else "",
                    "cena": cena,
                    "saite": saite
                })

            except ValueError:
                continue

    if not atrastie:
        print("Nav atrasts neviens produkts pēc dotajiem kritērijiem")
    else:
        print(f"\nAtrasti produkti starp {min_cena or 0:.2f}€ un {max_cena:.2f}€:\n")
        for i, prece in enumerate(atrastie, 1):
            print(f"{i}. {prece['nosaukums']}")
            print(f"   Apraksts: {prece['apraksts']}")
            print(f"   Cena: €{prece['cena']:.2f}")
            print(f"   Saites uz produktu: {prece['saite']}\n")


if __name__ == "__main__":
    print("\n-= IKEA labu cenu meklētājs =-")
    try:
        max_input = input("Ievadi MAKSIMĀLO cenu (€): ").strip()
        min_input = input("Ievadi MINIMĀLO cenu (€): ").strip()
        vardi_input = input("Ievadi meklējamos vārdus aprakstā: ").strip()

        max_cena = float(max_input)
        min_cena = float(min_input) if min_input else None
        atslegvardu_saraksts = vardi_input.lower().split() if vardi_input else None

        iegut_preces_filtrsetas(max_cena, min_cena, atslegvardu_saraksts)

    except ValueError:
        print("Lūdzu ievadi derīgas cenas kā skaitļus!")
