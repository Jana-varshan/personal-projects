import pandas as pd
import datetime
import smtplib
import random
from tkinter import *
from tkinter import messagebox

mail = "angelayutest@gmail.com"
password = "tzxpzsamqtoxzjys"

formats = ["Letter_1.txt", "Letter_2.txt", "Letter_3.txt"]

df = pd.read_csv("birthdays.csv")

name = df.iat[0, 0]
mail1 = df.iat[0, 1]
yr = df.iat[0, 2]
mon = df.iat[0, 3]
day = df.iat[0, 4]

date=[yr,mon,day]
now = datetime.datetime.now()
date1=[now.year,now.month,now.day]
d=""

if date== date1:
    let = random.choice(formats)
    with open(let, "r") as f:
        lst = f.readlines()
        newest = lst[0].split()
        newest[1] = f"{name},"
        lst[0] = newest[0] + " " + newest[1]
        for i in lst:
            d+=i

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=mail, password=password)
            connection.sendmail(from_addr=mail, to_addrs=mail1,
                                msg=f"Subject:Happy Birthday!!!\n\n"
                                    f"{d}")

