import smtplib
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase

if True:

    # humidity, temperature = Adafruit_DHT.read_retry(11, 4)

    # print 'Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity)

    fromaddr = ""
    toaddr = ""
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Room temperature"

    body = """
    Hello,
    """ + "message here"
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('mail.infomaniak.com', 25)
    server.starttls()
    server.login(fromaddr, "")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
    print("Message sent.")