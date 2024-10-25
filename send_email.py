import smtplib
import ssl

host = "smtp.gmail.com"
port = 465

username = "smithnathan2098@gmail.com"
password = "oshfsyuptenweuaq"

receiver = "smithnathan2098@gmail.com"

context = ssl.create_default_context()

message = """\
Subject: Hi!
Hello
"""

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)