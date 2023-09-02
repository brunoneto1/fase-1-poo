import requests
from bs4 import BeautifulSoup

url = "https://pt.wikipedia.org/wiki/Campeonato_Mundial_de_F%C3%B3rmula_1_de_2023"

# Faz a requisição HTTP e obtém o HTML da página
response = requests.get(url)
html = response.content

# Cria um objeto BeautifulSoup para analisar o HTML
soup = BeautifulSoup(html, "html.parser")

# Seleciona os elementos de título (por exemplo, <h1>, <h2>, <h3>, etc.)
titles = soup.find_all(["h1", "h2", "h3"])

# Abre o arquivo de saída em modo de escrita
with open("titulos.txt", "w", encoding="utf-8") as file:
    # Itera sobre os elementos de título e escreve no arquivo
    for title in titles:
        file.write(title.get_text() + "\n")

print("Títulos extraídos e salvos em 'titulos.txt'")
