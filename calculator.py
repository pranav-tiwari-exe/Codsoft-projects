from tkinter import *
from tkinter.font import Font

root=Tk()
root.title(" SIMPLE CALCULATOR ")
root.resizable(0,0)
var_ans=StringVar()
font_cal=Font(family="System",size=28)
font_but=Font(family="System",size=10)

e=Entry(root,width=15,font=font_cal,textvariable=var_ans,relief="flat")
e.config(bg="white",fg="Black",highlightcolor="black",highlightthickness=1,highlightbackground="black")
e.grid(row=0,column=1,columnspan=4,pady=20)

def button_num(number):
    e.insert(END,number)

def button_OP(oper):
    e.insert(END,oper)

def button_delete():
    current=var_ans.get()
    e.delete(str(len(current)-1))

def button_clean():
    e.delete(0,END)

def button_equals():
    s=var_ans.get()
    t_ans=eval(s)
    e.delete(0,END)
    e.insert(END,str(t_ans))


button_1=Button(root,text="1",padx=28,pady=20,relief="flat",font=font_but,command=lambda: button_num(1)).grid(row=4,column=1)
button_2=Button(root,text="2",padx=28,pady=20,relief="flat",font=font_but,command=lambda: button_num(2)).grid(row=4,column=2)
button_3=Button(root,text="3",padx=28,pady=20,relief="flat",font=font_but,command=lambda: button_num(3)).grid(row=4,column=3)
button_4=Button(root,text="4",padx=28,pady=20,relief="flat",font=font_but,command=lambda: button_num(4)).grid(row=3,column=1)
button_5=Button(root,text="5",padx=28,pady=20,relief="flat",font=font_but,command=lambda: button_num(5)).grid(row=3,column=2)
button_6=Button(root,text="6",padx=28,pady=20,relief="flat",font=font_but,command=lambda: button_num(6)).grid(row=3,column=3)
button_7=Button(root,text="7",padx=28,pady=20,relief="flat",font=font_but,command=lambda: button_num(7)).grid(row=2,column=1)
button_8=Button(root,text="8",padx=28,pady=20,relief="flat",font=font_but,command=lambda: button_num(8)).grid(row=2,column=2)
button_9=Button(root,text="9",padx=28,pady=20,relief="flat",font=font_but,command=lambda: button_num(9)).grid(row=2,column=3)
button_0=Button(root,text="0",padx=28,pady=20,relief="flat",font=font_but,command=lambda: button_num(0)).grid(row=5,column=2)

button_0=Button(root,text=".",padx=30,pady=20,relief="flat",font=font_but,command=lambda: button_OP(".")).grid(row=5,column=1)

button_mod=Button(root,text="%",relief="flat",padx=26,pady=20,font=font_but,command=lambda: button_OP("%")).grid(row=1,column=3)
button_plus=Button(root,text="+",relief="flat",padx=28,pady=20,font=font_but,command=lambda: button_OP("+")).grid(row=1,column=4)
button_minus=Button(root,text="-",relief="flat",padx=30,pady=20,font=font_but,command=lambda: button_OP("-")).grid(row=2,column=4)
button_multiply=Button(root,text="*",relief="flat",padx=30,pady=20,font=font_but,command=lambda: button_OP("*")).grid(row=3,column=4)
button_divide=Button(root,text="/",relief="flat",padx=30,pady=20,font=font_but,command=lambda: button_OP("/")).grid(row=4,column=4)


button_clear=Button(root,text="C",relief="flat",padx=27,pady=20,font=font_but,command= button_clean).grid(row=1,column=1)
button_cut=Button(root,text="<",relief="flat",padx=28,pady=20,font=font_but,command= button_delete).grid(row=1,column=2)

button_isequalto=Button(root,text="=",relief="flat",padx=68,pady=20,font=font_but,command= button_equals).grid(row=5,column=3,columnspan=2)




root.mainloop()