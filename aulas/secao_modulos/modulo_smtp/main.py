import os
import dotenv
import pathlib
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

ENV_LOCATION = os.path.join(pathlib.Path.home(), 'Documents\\GitHub\\CursoPython\\.env')
dotenv.load_dotenv(ENV_LOCATION)

# dados do remetente e destinatário
remetente = os.getenv("FROM_EMAIL")
destinatario = remetente

# configurações do SMTP
smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_username = os.getenv("FROM_EMAIL")
smtp_password = os.getenv("EMAIL_PASSWORD")

# Criando a mensagem do email
MESSAGE_TEMPLATE_PATH = os.path.join(pathlib.Path(__file__).parent, 'email.txt')

with open(MESSAGE_TEMPLATE_PATH, encoding="utf8") as file:
    template = Template(file.read())
    email_text = template.substitute(
        nome="Gustavo", from_email=remetente, to_email=destinatario
    )


"""
Vamos criar um objeto MIMEMultipart para compor a mensagem de e-mail. Este objeto nos permite definir o remetente, 
destinatário, assunto e corpo do e-mail.
"""

mail_subject = 'Teste de emails com python'
mail_body = email_text

email_message = MIMEMultipart()
email_message['From'] = remetente
email_message['To'] = destinatario
email_message['Subject'] = mail_subject
email_message.attach(MIMEText(mail_body))


def send_email(
        mail_from:str, mail_to:str, message:MIMEMultipart,
        smtp_server_:str, smtp_port_:int,
        smtp_username_:str, smtp_password_:str
):
    """tries to send an email"""
    with smtplib.SMTP(smtp_server_, smtp_port_) as server:
        server.ehlo()
        server.starttls()
        server.login(smtp_username_, smtp_password_)
        server.sendmail(from_addr=mail_from, to_addrs=mail_to, msg=message.as_string())
        print("Email enviado")


if __name__ == '__main__':
    send_email(remetente, destinatario, email_message, smtp_server, smtp_port, smtp_username, smtp_password)
