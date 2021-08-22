import smtplib, ssl

port = 465
smtp_server = "smtp.gmail.com"
sender_email = "testepython1204@gmail.com"
receiver_email = "carolina.lauffer@gmail.com", "gabriel.lauffer1@gmail.com"
password = ''  # digite sua senha
message = """\
Subject: Hi Mister.
Tenha um bom.""".encode('ascii', 'ignore')

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
