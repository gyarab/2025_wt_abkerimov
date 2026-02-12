import httpx
import sys
from colorama import Fore, Style, init

init(autoreset=True)

URL = "https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt"

try:
    with httpx.Client() as client:
        res = client.get(URL)
        res.raise_for_status()
except httpx.HTTPError as e:
    print(Fore.RED + f"Chyba při stahování dat z ČNB: {e}")
    sys.exit(1)

lines = res.text.splitlines()
header = lines[0].split(" #")[0]

line_euro = next((line for line in lines if "EUR" in line), None)

if not line_euro:
    print(Fore.RED + "V kurzovním lístku nebylo nalezeno EUR.")
    sys.exit(1)

parts = line_euro.split('|')
rate = float(parts[-1].replace(',', '.'))

print(Fore.CYAN + "=" * 40)
print(Fore.YELLOW + f" Kurzy ČNB pro den: {header}")
print(Fore.CYAN + "=" * 40)
print(f" Aktuální kurz: {Fore.WHITE}1 EUR = {rate} CZK")
print(Fore.CYAN + "-" * 40)

print("Vyberte směr převodu:")
print(f"{Fore.MAGENTA}1:{Style.RESET_ALL} EUR -> CZK")
print(f"{Fore.MAGENTA}2:{Style.RESET_ALL} CZK -> EUR")

volba = input(Fore.BLUE + "Vaše volba (1/2): ").strip()

try:
    if volba == "1":
        vstup = input("Zadejte částku v EUR: ").replace(',', '.')
        castka = float(vstup)
        vysledek = castka * rate
        print(Fore.GREEN + f"-> {castka} EUR = {vysledek:.2f} CZK")
    elif volba == "2":
        vstup = input("Zadejte částku v CZK: ").replace(',', '.')
        castka = float(vstup)
        vysledek = castka / rate
        print(Fore.GREEN + f"-> {castka} CZK = {vysledek:.2f} EUR")
    else:
        print(Fore.RED + "Neplatná volba. Spusťte program znovu a vyberte 1 nebo 2.")
except ValueError:
    print(Fore.RED + "Chyba: Zadaná hodnota není platné číslo.")

print(Fore.CYAN + "=" * 40)
