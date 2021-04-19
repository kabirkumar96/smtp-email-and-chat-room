import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP('smtp.google.com: 587')

server.ehlo()

# it's better to keep an encrypted your password in a text file
# then decrypt to use here
# with open('password.txt', 'r') as f:
#     password = f.read()

server.login('email@email.com', 'password')

message = MIMEMultipart()
message['From'] = 'Sender'
message['To'] = 'target@mail.com'
message['Subject'] = 'Just A Sample SMTP Mail'

with open('msg.txt', 'r') as f:
    msg = f.read()

message.attach(MIMEText(msg, 'plain'))

filename = 'PainfulHarold.jpg'
attachment = open(filename, 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename={filename}')
message.attach(p)

text = message.as_string()
server.sendmail('iamkabir11@gmail.com', 'kabirkumar11@gmail.com', text)