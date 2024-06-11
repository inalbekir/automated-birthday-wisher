# import smtplib
#
my_email = "oldbutbronz@gmail.com"
my_password = "xkpj hxsq ybeq yhwz"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=my_password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="bekirinal5415@gmail.com",
#         msg="Subject:Hello\n\nThis is the body of my email"
#     )

# import datetime as dt
#
# now = dt.datetime.now()
# day = now.weekday()
#
#
# date_of_birth = dt.datetime(year=2005, month=8, day=2)
# print(date_of_birth)

import datetime as dt
import smtplib
import random

day_of_week = dt.datetime.now().weekday()
if day_of_week == 1:
    with open("quotes.txt") as file:
        quote_file = file.readlines()
        quote = random.choice(quote_file)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="bekirinal5415@gmail.com",
            msg=f"Subject:Quote of the beautiful monday...\n\n{quote}"
     )
