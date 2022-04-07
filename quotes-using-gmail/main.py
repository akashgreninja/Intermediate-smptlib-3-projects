


import datetime as dt
import random
import smtplib
from email.message import EmailMessage

my_email = "Your-email"
password = "Your-password"
other_email = "Reciever's email"

with open(file="quotes.txt" ,mode="r") as quotes:
    new=quotes.readlines()
    random_quotes=random.choice(new)
    # print(random_quotes)


now = dt.datetime.now()
day = now.weekday()
if day == 3:
    msg = EmailMessage()
    msg.set_content(random_quotes)

    msg['Subject'] = 'Quotes'
    msg['From'] = my_email
    msg['To'] = other_email

    # Send the message via our own SMTP server.
    with smtplib.SMTP('smtp.gmail.com', port=587) as server:
        server.starttls()
        server.login(my_email, password=password)
        server.send_message(msg)
        server.close()

