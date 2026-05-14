

import requests
from bs4 import BeautifulSoup

print("Nova Digital IA - Iniciando Extracción...")
res = requests.get("https://www.google.com")
soup = BeautifulSoup(res.text, 'html.parser')
print("Resultado:", soup.title.string)

