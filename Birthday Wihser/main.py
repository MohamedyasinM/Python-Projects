import smtplib
import random
import pandas
from datetime import *



today = datetime.now()
tuple_date = (today.day,today.month)


data = pandas.read_csv("birthdays.csv")


data_dict = {(row.day,row.month) : row for (index,row) in data.iterrows()}


for d in data_dict:
    if d == tuple_date:
        Name = data_dict[d]["name"]
        file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"

        with open(file_path , mode="r") as letter:
            content = letter.read()
            se_letter = content.replace("[NAME]",Name)

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login("yasindevelopment10@gmail.com","xootryuehsawgnfq")
            connection.sendmail(from_addr="yasindevelopment10@gmail.com",
                                to_addrs=data_dict[d]["email"],
                                msg=f"Subject:Happy birthday :)\n\n{se_letter}")

