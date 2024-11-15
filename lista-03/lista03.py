import requests
from bs4 import BeautifulSoup

url = "https://example.com"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    title = soup.title.string if soup.title else "Sem título"
    print("Título da página:", title)

    print("\nLinks encontrados:")
    for link in soup.find_all('a'):
        href = link.get('href')
        if href:
            print(href)
else:
    print("Erro ao acessar a página:", response.status_code)
