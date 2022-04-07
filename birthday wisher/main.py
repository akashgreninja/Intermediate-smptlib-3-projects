import datetime as tk
import random
import smtplib
from email.message import EmailMessage
import pandas



my_email = "Your-email"
password = "Your-password"
other_email = "Reciever's email"


now=tk.datetime.now()
day=now.date()
today=(now.month,now.day)

data=pandas.read_csv("birthdays.csv")






a=random.randint(1,3)

birthdays_dict={(value.month,value.day) :value  for(index,value) in data.iterrows() }
print(birthdays_dict)

if today in  birthdays_dict:
    birthdays_person=birthdays_dict[today]
    print(birthdays_person)
    file_path=f"letter_templates/letter_{a}.txt"
    with open(file=file_path) as file:

        z=file.read()
        u=z.replace("[NAME]",birthdays_person["name"])



    msg = EmailMessage()
    msg.set_content(u)

    msg['Subject'] = 'Happy Birthday'
    msg['From'] = my_email
    msg['To'] = birthdays_person.email

    # Send the message via our own SMTP server.
    with smtplib.SMTP('smtp.gmail.com', port=587) as server:
        server.starttls()
        server.login(my_email, password=password)
        server.send_message(msg)
        server.close()






