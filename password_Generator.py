from tkinter import *
import string
import random

def generate_password(length):
    l=(length.get())
    ch= string.ascii_letters + string.punctuation + string.digits
    password= ''.join(random.choice(ch) for _ in range(l))
    return password

def print_password():
    l=var_1
    ANS=generate_password(l)
    l_2.config(text=("Password Generated is:"))
    l_result.config(text=ANS,fg="red")
    


window=Tk()
window.title("Password Generator:")
window.geometry('400x100+600+350')
var_1=IntVar()

l_1=Label(window,text="Enter the Length of the Password to be Generated:").pack()

e_1=Entry(window,textvariable=var_1).pack()

but_1=Button(window,text=("SUBMIT"),command=print_password).pack()

fr=Frame(window)

l_2=Label(fr,text="")

l_result=Label(fr,text="")

fr.pack()

l_2.pack(side="left")

l_result.pack(side="left")


window.mainloop()
