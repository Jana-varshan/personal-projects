import pandas as pd
import datetime
import smtplib
import random
from tkinter import *
from tkinter import messagebox

# ans=input("do you want to add data ?")
# # ui setup
# while ans=="yes":
#     window = Tk()
#     window.title("birthday wisher")
#     window.config(pady=20,padx=20,background="light blue")
#
#     # canvas= Canvas(height=300,width=300)
#     # canvas.grid(column=1,row=1)
#     label_n=Label(text="Name:",font=("arial",18,"italic bold"),background="light blue")
#     label_n.grid(column=1,row=2)
#     label_n.config(pady=10,padx=10)
#
#     label_m=Label(text="Mail id:",font=("arial",18,"italic bold"),background="light blue")
#     label_m.grid(column=1,row=3)
#     label_m.config(pady=10,padx=10)
#
#     label_d=Label(text="DOB:",font=("arial",18,"italic bold"),background="light blue")
#     label_d.grid(column=1,row=4)
#     label_d.config(pady=10,padx=10)
#
#     name=Entry(width=36)
#     name.grid(column=2,row=2,columnspan=2)
#
#     mail=Entry(width=36)
#     mail.grid(column=2,row=3,columnspan=2)
#
#     mail=Entry(width=20)
#     mail.grid(column=2,row=4)
#
#     lab_h=Label(text="Data base entry",font=("arial",24,"italic bold"))
#     lab_h.grid(column=1,row=1,columnspan=2)
#
#     window.mainloop()
#mind


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

