import datetime as dt
import smtplib
import random

my_email = "sender's_email_id"
password = "sender's_password"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 1:
    with open("Birthday Wisher Email/quotes.txt") as quote_file:
        quotes = quote_file.readlines()
        quote = random.choice(quotes)
    
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls() #provides encryption
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
        to_addrs="receiver's email address",
        msg="Subject:Monday Motivation \n\n {quote}"
        )