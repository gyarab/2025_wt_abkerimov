import httpx

r = httpx.get('https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt')
print(r.text)
print(r.status_code)
lines = r.text.split('\n')
print(lines[0])

line_euro = ""
for line in lines:
    if "EUR" in line:
        line_euro = line
        break

rate_str = line_euro.split('|')[-1].replace(',', '.')
rate = float(rate_str)

print(f"Current EUR/CZK rate: {rate}")

value_in = float(input("Enter amount in EUR: "))

vlaue_out = value_in * rate
print(f"Your's {value_in} EUR is {vlaue_out} CZK at the current rate.")
