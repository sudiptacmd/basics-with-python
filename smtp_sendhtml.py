import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os
from dotenv import load_dotenv

load_dotenv()

sender = "amionekshadhu@outlook.com"
receiver = "pragga.frc@gmail.com"
password = os.environ['SMTPASS']

message = MIMEMultipart()
message['From'] = sender
message['To'] = receiver
message['Subject'] = "ATTACHMENT DISII HTML"

body = """
<h1> Kire Mama eida heding</h1>
<br>
<h3 style="color:blue"> EIDA NIL MAMA </h3>
"""

attachment_path = "files/H.avif"
file = open(attachment_path, 'rb')
payload = MIMEBase('application', 'octate-stream')
payload.set_payload(file.read())
encoders.encode_base64(payload)
payload.add_header('Content-Disposition', 'attachment', filename="H.avif")
message.attach(payload)

mimetext = MIMEText(body, "html")
message.attach(mimetext)
message_f = message.as_string()
server = smtplib.SMTP('smtp.office365.com', 587)
server.starttls()
server.login(sender, password)
server.sendmail(sender, receiver, message_f)
server.quit()