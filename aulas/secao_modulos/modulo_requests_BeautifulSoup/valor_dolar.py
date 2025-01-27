from bs4 import BeautifulSoup
import requests

response = requests.get("https://wise.com/br/currency-converter/dolar-hoje")

# Um objeto BeautifulSoup funciona de forma parecida com o objeto DOM do JS
html = BeautifulSoup(response.text, "html.parser")

# retorna a tag com o identificador passado
txtbox_reais = html.select_one("#target-input")

# resgatando o atributo 'value' dessa tag
dollar_in_reais = txtbox_reais.get("value")
print(f"USA $1.00 = BRL R${dollar_in_reais}")
