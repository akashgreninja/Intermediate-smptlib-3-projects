import smtplib
from email.message import EmailMessage

# from smtplib import SMTP
#
my_email="Your-email"
password="Your-pass"
other_email="Recievers mail"


#This is the old method but still works scroll down for a better method


# connection=SMTP("smtp.gmail.com",port=587)
# connection.starttls()
# connection.login(user=my_email,password=password)
# connection.sendmail(from_addr=my_email,to_addrs=other_email,msg="Subject:hello world\n\nThis is my first email")
# connection.close()
# print("closed")



#better method to send emails from StackOverflow here the email is not secured while using thr SMTP_SSL so preferred to use SMTP class

import smtplib
from email.message import EmailMessage

msg = EmailMessage()
msg.set_content('This is my message')

msg['Subject'] = 'Subject'
msg['From'] = my_email
msg['To'] = other_email

# Send the message via our own SMTP server.
with smtplib.SMTP('smtp.gmail.com', port=587) as server:
    server.starttls()
    server.login(my_email, password=password)
    server.send_message(msg)
    server.close()
