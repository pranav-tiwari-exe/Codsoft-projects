#importing required modules.
from tkinter import *
import string
import random

def generate_password(length):                                   #Function for generating password.
    l=(length.get())
    ch= string.ascii_letters + string.punctuation + string.digits
    password= ''.join(random.choice(ch) for _ in range(l))
    return password

def print_password():                                            #Function for printing password.
    l=var_1
    ANS=generate_password(l)
    l_2.config(text=("Password Generated is:"))
    l_result.config(text="\n"+ANS+"\n",fg="red",wraplength=200)

window=Tk()                                                      #creating GUI Window.
window.title("Password Generator:")                              #giving title
window.geometry('450x200+600+350')                               #setting up dimensions
window.resizable(width=False,height=True)                        #locking dimensions
window.configure(bg="white")                                     #setting background color

#Creating elements in the GUI window and setting their properties
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

window.mainloop()                                                  #infinity loop of GUI window ,so that it dosen't close
