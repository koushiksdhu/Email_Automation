import pandas as pd
from datetime import datetime as dt
import smtplib

email = "ksprojecttesting@gmail.com"
password = "kgnpcimslpnaxtrh"
PORT = 587  # PORT number should be 587.

birthday_csv = pd.read_csv("birthday.csv")
birthday_dict_list = birthday_csv.to_dict(orient = "records")
# print(birthday_dict_list)

current_datetime = dt.now()
month = current_datetime.month
day = current_datetime.day

todays_date = (day, month)
# print(todays_date)

for person in birthday_dict_list:
    person_bday_date = (person["Day"], person["Month"])
    if(person_bday_date == todays_date):    
        with open("letter.txt") as data:
            message = data.read()
            message = message.replace("[NAME]", person["Name"])
            print(message)
         
        with smtplib.SMTP("smtp.gmail.com", port = 587) as connection:
            connection.starttls()
            connection.login(user = email, password = password)
            connection.sendmail(
                from_addr = email,
                to_addrs = "kkoushikssadhu@gmail.com",
                msg = f"Subject: Happy Birthday!\n\n{message}"
            )
            connection.quit()
            
    