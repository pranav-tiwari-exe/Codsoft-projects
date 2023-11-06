from tkinter import *
import random
from tkinter.font import Font

def R_P_S(u_choice):
    l=["Rock","Paper","Sissor"]
    c_choice=random.choice(l)
    if u_choice==c_choice:
        comp_choice.config(text=c_choice.upper())
        user_choice.config(text=c_choice.upper())
        result.config(text="  DRAW",fg="black")
    elif u_choice=="Rock" and c_choice=="Sissor":
        comp_choice.config(text="SISSOR")
        user_choice.config(text="ROCK")
        result.config(text=" YOU WON",fg="green")
    elif u_choice=="Sissor" and c_choice=="Paper":
        comp_choice.config(text="PAPER")
        user_choice.config(text="SISSOR")
        result.config(text=" YOU WON",fg="green")
    elif u_choice=="Paper" and c_choice=="Rock":
        comp_choice.config(text="ROCK")
        user_choice.config(text="PAPER")
        result.config(text=" YOU WON",fg="green")
    else :
        comp_choice.config(text=c_choice.upper())
        user_choice.config(text=u_choice.upper())
        result.config(text=" YOU LOST",fg="RED")

root=Tk()
root.title("Rock-Paper_Sissors")
root.geometry("450x450+550+150")
root.resizable(0,0)

rsp_font1=Font(
    family="IMPACT",
    size=25)

rsp_font2=Font(
    family="System",
    size=5,weight="bold")

rsp_font3=Font(
    family="System",
    size=20,weight="bold")

l_1=Label(root,text="CHOOSE FROM THE FOLLOWING",padx=30,pady=20,font=rsp_font1).grid(row=0,column=0,columnspan=6)


comp_choice=Label(root,text="",font=rsp_font3)
user_choice=Label(root,text="",font=rsp_font3)
result=Label(root,text="",font=rsp_font3,pady=50)
vs=Label(root,text="V/S",font=("System",30),fg="orange",pady=70)

rock_bt=Button(root,text="ROCK",command=lambda: R_P_S("Rock"),padx=50,pady=30,font=rsp_font2,relief=GROOVE).grid(row=1,column=0,columnspan=2)
paper_bt=Button(root,text="PAPER",command=lambda: R_P_S("Paper"),padx=50,pady=30,font=rsp_font2,relief=GROOVE).grid(row=1,column=3,columnspan=2)
sissor_bt=Button(root,text="SISSOR",command=lambda: R_P_S("Sissor"),padx=50,pady=30,font=rsp_font2,relief=GROOVE).grid(row=1,column=5,columnspan=2)

cop=Label(root,text="COMPUTER'S\nCHOICE:",pady=40,font=rsp_font2).grid(row=2,column=0,columnspan=3)
usr=Label(root,text="YOU\nCHOICE:",pady=40,font=rsp_font2).grid(row=2,column=5,columnspan=2)

comp_choice.grid(row=3,column=1)
user_choice.grid(row=3,column=5)
vs.grid(row=2,column=3,columnspan=2,rowspan=2)
result.grid(row=4,column=3)

root.mainloop()