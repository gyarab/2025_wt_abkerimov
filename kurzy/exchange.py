import httpx

r = httpx.get('https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt?date=21.01.2026')
print(r.text)
print(r.status_code)
lines = r.text.split('\n')
print(lines[0])
