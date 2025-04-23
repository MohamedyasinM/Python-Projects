import datetime
import smtplib
import random

# today = datetime.datetime.now()
# year = today.year
# month = today.month
# day_ = today.weekday()
#
#
# print(today,"    ",year,"   ",month,"daty :",day_)
mail = "yasindevelopment10@gmail.com"
password = "xootryuehsawgnfq"

today = datetime.datetime.now()
day_ = today.weekday()

if day_==1:
    with open("quotes.txt") as quote:
        all_quotes = quote.readlines()

    quote = random.choice(all_quotes)
    with smtplib.SMTP("smtp.gmail.com") as con:
        con.starttls()
        con.login(user=mail,password=password)
        con.sendmail(from_addr=mail,
                     to_addrs="mohamedyasin25808@gmail.com",
                     msg=f"Subject:Monday Motivational Quote\n\n Hi Yasin,\n{quote}")
        con.close()

