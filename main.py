import datetime as dt
import random
import smtplib

now=dt.datetime.now()

day=now.day
month=now.month

myday = 11
mymonth = 6

user_name="pandiyankrishna2001@gmail.com"

password="akdw uuor qqso vwbt"

smtp_server= "smtp.gmail.com"
port=587

if day==myday and month==mymonth:
    with open("quote.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP(smtp_server, port) as connection:
        connection.starttls()
        connection.login(user_name, password)
        connection.sendmail(
            from_addr=user_name,
            to_addrs="pandiyan.it20@bitsathy.ac.in",
            msg=f"Subject:motivation\n\n {quote}"
        )    
