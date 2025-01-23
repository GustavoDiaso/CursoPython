import os
import dotenv
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

dotenv.load_dotenv(r"C:\Users\Gustavo\Documents\GitHub\CursoPython\.env")

# dados do remetente e destinatário
remetente = os.getenv("FROM_EMAIL")
destinatario = remetente

# configurações do SMTP
smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_username = os.getenv("FROM_EMAIL")
smtp_password = os.getenv("EMAIL_PASSWORD")

# Mensagem de texto
caminho_msg = "C:\\Users\\Gustavo\\Documents\\GitHub\\CursoPython\\aulas\\secao_modulos\\modulo_smtp\\email.txt"

with open(caminho_msg, "r", encoding="utf8") as file:
    texto_arquivo = file.read()
    template = Template(texto_arquivo)
    texto_email = template.substitute(
        nome="Gustavo", from_email=remetente, to_email=destinatario
    )


def send_email():
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.ehlo()
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(from_addr=remetente, to_addrs=destinatario, msg="Olá ")
        print("Email enviado")


send_email()
