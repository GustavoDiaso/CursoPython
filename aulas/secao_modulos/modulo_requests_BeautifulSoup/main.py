# (Parte 1) Básico do protocolo HTTP (HyperText Transfer Protocol)
# HTTP (HyperText Transfer Protocol) é um protocolo usado enviar e receber
# dados na Internet. Ele funciona no modo cliente/servidor, onde o cliente
# (seu navegador, por exemplo) faz uma requisição ao servidor
# (site, por exemplo), que responde com os dados adequados.
#
# A mensagem de requisição do cliente deve incluir dados como:
# - O metodo HTTP
#     - leitura (safe) - GET, HEAD (cabeçalhos), OPTIONS (métodos suportados)
#     - escrita - POST, PUT (substitui), PATCH (atualiza), DELETE
# - O endereço do recurso a ser acessado (/users/)
# - Os cabeçalhos HTTP (Content-Type, Authorization)
# - O Corpo da mensagem (caso necessário, de acordo com o metodo HTTP)
#
# A mensagem de resposta do servidor deve incluir dados como:
# - código de status HTTP (200 success, 404 Not found, 301 Moved Permanently)
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
# - Os cabeçalhos HTTP (Content-Type, Accept)
# - O corpo da mensagem (Pode estar em vazio em alguns casos)

# O módulo requests consegue carregar dados da Internet para dentro do seu
# código. Já o bs4.BeautifulSoup é responsável por interpretar os dados HTML
# em formato de objetos Python para facilitar a vida do desenvolvedor.

# Tutorial Requests -> https://youtu.be/Qd8JT0bnJGs
# Biblioteca Beautiful Soup  - Doc: https://www.crummy.com/software/BeautifulSoup/bs4/doc.ptbr/

# modulo para fazer requisições
import requests
from bs4 import BeautifulSoup

url = "http://localhost:3333/"

response = requests.get(url=url)
raw_html = response.text
# print("Status Code:", response.status_code)
# print(raw_html)

# Html em formato objeto python
parsed_html = BeautifulSoup(raw_html, "html.parser", from_encoding="utf-8")

print(parsed_html.title)
print(parsed_html.title.text)

top_jobs_heading = parsed_html.select_one("#intro > div > div > article > h2")
print(top_jobs_heading.text)

# pegando elemento pai do nosso <h2>TOP 3 JOBS<\h2>
article = top_jobs_heading.parent

if article is not None:
    for paragraph in article.select("p"):
        print(paragraph.text.strip())

"""
-> htmlobject.select_one: retorna apenas um dos objetos com a tag especificada 
-> htmlobject.select: retorna todos os objetos com a tag especificada.
"""
