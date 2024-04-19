import random
from tkinter import *
from tkinter import messagebox

import json
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password_char = "".join(password_list)

    password.insert(0, password_char)

    pyperclip.copy(password_char)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_func():
    website_name = web.get()
    email = mail.get()
    password_web = password.get()
    new_dic = {
        website_name: {
            "email": email,
            "password": password_web
        }
    }

    if len(website_name) == 0:
        messagebox.showinfo(title="error", message="Please dont leave any empty boxes!!")

    elif len(password_web) == 0:
        messagebox.showinfo(title="error", message="Please dont leave any empty boxes!!")

    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_dic, data_file, indent=4)

        else:
            data.update(new_dic)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:

            web.delete(0, END)
            password.delete(0, END)


def search_fun():
    web_name=web.get()
    with open("data.json", "r") as data_file:
        data = json.load(data_file)
    try:
        new=data[web_name]
    except KeyError:
        messagebox.showinfo(title="Error",message="Invalid input!!")

    else:
        email_new=new["email"]
        pass_new=new["password"]
        messagebox.showinfo(title="Information",message=f"Email={email_new}\n Password={pass_new}")



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(75, 100, image=img)
canvas.grid(column=1, row=0, columnspan=3)

# website input
img
label_web = Label(text="Website:")
label_web.grid(column=0, row=1)

web = Entry(width=35)
web.focus()
web.grid(column=1, columnspan=3, row=1,)
# mail input
label_mail = Label(text="Email/Username:")
label_mail.grid(column=0, row=2)

mail = Entry(width=65)
mail.insert(0, "Example@gmail.com")
mail.grid(column=2, columnspan=4, row=2)

# pass input
label_pass = Label(text="Password:")
label_pass.grid(column=0, row=3)

password = Entry(width=35)
password.grid(column=2, row=3, columnspan=1)

# generate butt
generate_butt = Button(text="Generate Password", command=password_generator,width=20)
generate_butt.grid(column=4, row=3, columnspan=4)

# add butt
add_butt = Button(text="Add", width=60, command=add_func)
add_butt.grid(column=1, columnspan=4, row=4, pady=10)

# search butt
search_butt = Button(text="search",width=20,command=search_fun)
search_butt.grid(column=4,row=1,columnspan=3,padx=10)

window.mainloop()
