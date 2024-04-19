from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("birthday wisher")
window.config(pady=20,padx=20,background="light blue")

# canvas= Canvas(height=300,width=300)
# canvas.grid(column=1,row=1)
label_n=Label(text="Name:",font=("arial",18,"italic bold"),background="light blue")
label_n.grid(column=1,row=2)
label_n.config(pady=10,padx=10)

label_m=Label(text="Mail id:",font=("arial",18,"italic bold"),background="light blue")
label_m.grid(column=1,row=3)
label_m.config(pady=10,padx=10)

label_d=Label(text="DOB:",font=("arial",18,"italic bold"),background="light blue")
label_d.grid(column=1,row=4)
label_d.config(pady=10,padx=10)

name=Entry(width=36)
name.grid(column=2,row=2,columnspan=2)

mail=Entry(width=36)
mail.grid(column=2,row=3,columnspan=2)

mail=Entry(width=20)
mail.grid(column=2,row=4)

lab_h=Label(text="Data base entry",font=("arial",24,"italic bold"))
lab_h.grid(column=1,row=1,columnspan=2)

window.mainloop()