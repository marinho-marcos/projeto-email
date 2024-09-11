import os
import smtplib
from email.message import EmailMessage
from password import senha

EMAIL_ADDRESS = "marcosmarinho485@gmail.com"
EMAIL_PASSWORD = senha

#CORPO DO EMAIL
msg = EmailMessage()
msg['Subject'] = input("Assunto -> ")
msg['From'] = EMAIL_ADDRESS
msg['To'] = input("E-mail de destino -> ")
msg.set_content(input("Digite a mensagem a ser enviada -> "))

#REALIZANDO LOGIN E ENVIANDO EMAIL
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)




import os
import smtplib
from email.message import EmailMessage
from password import senha

EMAIL_ADDRESS = "marcosmarinho485@gmail.com"
EMAIL_PASSWORD = senha

#CORPO DO EMAIL
msg = EmailMessage()
msg['Subject'] = input("Assunto -> ")
msg['From'] = EMAIL_ADDRESS
msg['To'] = input("E-mail de destino -> ")
msg.set_content(input("Digite a mensagem a ser enviada -> "))

#REALIZANDO LOGIN E ENVIANDO EMAIL
try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
        print("E-mail enviado com sucesso!")  # Mensagem de confirmação
except smtplib.SMTPException as e:
    print(f"Falha no envio do e-mail: {e}")  # Mensagem de erro
