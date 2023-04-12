import tkinter
screen=tkinter.Tk()
screen.geometry("400x400")

# tkinter variable
email_var=tkinter.StringVar()
password_var=tkinter.StringVar()
msg_var=tkinter.StringVar()

# python function
def myfun():
    msg_var.set(email_var.get())

# label display
lbl=tkinter.Label(screen,text="Login Form",font=("Arial",26,"bold"))
lbl.pack()

# entry display
el_lbl=tkinter.Label(screen,text="Enter Email",font=("Arial",10,"bold"))
el_lbl.place(x=50,y=55)
el=tkinter.Entry(screen,textvariable=email_var)
el.place(x=180,y=60)

# password display
el_lbl=tkinter.Label(screen,text="Enter Password",font=("Arial",10,"bold"))
el_lbl.place(x=50,y=95)
el=tkinter.Entry(screen,textvariable=password_var)
el.place(x=180,y=102)

# button display
btn=tkinter.Button(screen,text="SIGN IN",font=("Arial",8,"bold"),command=myfun)
btn.place(x=180,y=130)

# final msg display
lbl_msg=tkinter.Label(screen,text="Message",textvariable=msg_var)
lbl_msg.place(x=180,y=160)

screen.mainloop()