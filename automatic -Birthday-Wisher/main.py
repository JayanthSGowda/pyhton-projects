import datetime as dt
import random
import smtplib
import pandas as pd

my_email = "YOUR MAIL HERE"
google_app_password = "YOUR PASSWORD HERE"
letters = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]

now = dt.datetime.now()
data = pd.read_csv("birthdays.csv")

name = data[(data.month == now.month) & (data.day == now.day)]
birthday_guys = name.to_dict(orient="records")
for person in birthday_guys:
    letter_temp = random.choice(letters)
    with open(letter_temp) as letter_data:
        letter = letter_data.read().replace("[NAME]", person["name"])
    with smtplib.SMTP("smtp.gmail.com") as connection:                      # "SMTP.GMAIL.COM" CHANGES FOR DIFFERENT SERVICE PROVIDER
        connection.starttls()
        connection.login(user=my_email, password=google_app_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=person['email'],
            msg=f"Subject:Happy birthday\n\n{letter}"
        )

