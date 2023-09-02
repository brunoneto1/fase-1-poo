import requests
from bs4 import BeautifulSoup
import csv


url = 'https://pt.wikipedia.org/wiki/Michael_Jackson'


response = requests.get(url)


if response.status_code == 200:
  
    soup = BeautifulSoup(response.text, 'html.parser')

    
    info_elements = soup.find_all('td', {'style': 'vertical-align: top; text-align: left;'})

    
    data = []

    
    for info in info_elements:
        data.append(info.get_text(strip=True))

    
    attribute_value_pairs = [data[i:i+2] for i in range(0, len(data), 2)]

    
    with open('michael_jackson_info.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Atributo', 'Valor']
        writer = csv.writer(csvfile)

        writer.writerow(['Atributo', 'Valor'])  # Cabeçalho do CSV

        for attribute, value in attribute_value_pairs:
            
            writer.writerow([f"{attribute}:", value])

    print('Dados extraídos e salvos em michael_jackson_info.csv')
else:
    print('Não foi possível acessar a página da Wikipedia.')

