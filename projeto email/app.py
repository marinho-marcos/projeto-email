import os
import smtplib
from email.message import EmailMessage
from password import senha

EMAIL_ADDRESS = "marcosmarinho485@gmail.com"
EMAIL_PASSWORD = senha

msg = EmailMessage()
msg['Subject'] = "Teste de encaminhamento"
msg['From'] = "marcosmarinho485@gmail.com"
msg['To'] = "user2protocolos@gmail.com"
msg.set_content('TESTANDO THUNDERBIRD!!!!!!!!!!!!!!!!!!!!!!!!')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)