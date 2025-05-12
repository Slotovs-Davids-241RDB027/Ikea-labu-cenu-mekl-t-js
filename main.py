import requests
from bs4 import BeautifulSoup

def iegut_preces_lidz_cenai(max_cena):
    url = "https://www.ikea.lv/lv/last-chance"
    atbilde = requests.get(url)

    if atbilde.status_code != 200:
        print("Neizdevās ielādēt lapu")
        return

    soup = BeautifulSoup(atbilde.content, "html.parser")
    bloka = soup.find_all(class_="itemBlock")

    atrastas_preces = []

    for prece in bloka:
        nosaukums_elem = prece.find("h3")
        apraksts_elem = prece.find("h4", class_="itemFacts")
        cenas_elem = prece.find("span", {"data-price": True})
        saite_elem = prece.find("a", href=True)

        if nosaukums_elem and cenas_elem and saite_elem:
            try:
                cena = float(cenas_elem["data-price"])
                if cena <= max_cena:
                    saite = saite_elem["href"]
                    if not saite.startswith("http"):
                        saite = "https://www.ikea.lv" + saite

                    atrastas_preces.append({
                        "nosaukums": nosaukums_elem.get_text(strip=True),
                        "apraksts": apraksts_elem.get_text(strip=True) if apraksts_elem else "",
                        "cena": cena,
                        "saite": saite
                    })
            except ValueError:
                continue

    if not atrastas_preces:
        print("Nav atrasts neviens produkts šajā cenu diapazonā")
    else:
        print(f"\nAtrasti produkti zem {max_cena:.2f} EUR:\n")
        for i, prece in enumerate(atrastas_preces, 1):
            print(f"{i}. {prece['nosaukums']}")
            print(f"   Apraksts: {prece['apraksts']}")
            print(f"   Cena: €{prece['cena']:.2f}")
            print(f"   Saites uz produktu: {prece['saite']}\n")


if __name__ == "__main__":
    try:
        print("\n-=Labu cenu meklētājs=-")
        lietotaja_cena = float(input("Ievadi maksimālo cenu (€): "))
        iegut_preces_lidz_cenai(lietotaja_cena)
    except ValueError:
        print("Lūdzu ievadi pareizu skaitli!")
