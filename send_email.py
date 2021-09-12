import smtplib
from email.mime.text import MIMEText

def send_email():
    smtp_ssl_host = 'smtp.gmail.com'  # smtp.mail.yahoo.com
    smtp_ssl_port = 465
    username = 'email'
    password = 'pass'
    sender = 'mayur.sonawala13@gmail.com'
    targets = ['mayur.sonawala13@gmail.com']

    msg = MIMEText('Hi, how are you today?')
    msg['Subject'] = 'Hello'
    msg['From'] = sender
    msg['To'] = ', '.join(targets)

    server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
    server.login(username, password)
    server.sendmail(sender, targets, msg.as_string())
    server.quit()