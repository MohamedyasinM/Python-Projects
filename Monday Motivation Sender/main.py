import smtplib

mail = "yasindevelopment10@gmail.com"
password = "xootryuehsawgnfq"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=mail,password=password)
    connection.sendmail(from_addr=mail,
                        to_addrs="mohamedyasin25808@gmail.com",
                        msg="Subject:TestMail\nInside the Mail Body")
    connection.close()