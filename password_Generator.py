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
    l_result.config(text="\n"+ANS+"\n",fg="red",wraplength=200)

window=Tk()
window.title("Password Generator:")
window.geometry('450x200+600+350')
window.resizable(width=False,height=True)
window.configure(bg="white")


var_1=IntVar()

l_1=Label(window,text="PASSWORD GENERATION TOOL",font=("System",18),bg="white").pack()

l_=Label(window,text="\nEnter Password Length\n",font=("arial bold",10),bg="white").pack()

e_1=Entry(window,textvariable=var_1,width=24,relief="flat",bg="silver").pack()

but_1=Button(window,text=("GENERATE"),font=("calibri bold",10),command=print_password,width=20,relief='flat',bg="tomato").pack()

fr=Frame(window,bg="white")

l_2=Label(fr,text="",font=("Arial",10),bg="white")

l_result=Label(fr,text="",font=("Arial",10),bg="white")

fr.pack(side=BOTTOM)

l_2.pack(side="left")

l_result.pack(side="left")

window.mainloop()
