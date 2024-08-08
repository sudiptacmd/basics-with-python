import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

sender = "amionekshadhu@outlook.com"
receiver = "technet.sudipta@gmail.com"
password = os.environ['SMTPASS']
message = """\
Subject: Mama hello

Kemon asos
"""
print(message)
server = smtplib.SMTP('smtp.office365.com', 587)
server.starttls()
server.login(sender, password)
server.sendmail(sender, receiver, message)
server.quit()