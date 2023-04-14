# tkinter_example
import tkinter 
screen = tkinter.Tk() # screen define
screen.title("My First Application") # use for set the title 
screen.geometry("500x500") # use for  screen size
# python function
def myfun():
    print("This is my python Function")
#display specific widget
#lbl = tkinter.Label(screen,text="Hello welcome to tkinter",font=("Arial",26,"bold"))
#lbl.pack()   if you want top and center use pack method
#lbl.place(x = 20,y= 50) # place method use for manuaaly place something in application
#btn1 = tkinter.Button(screen,text="Click Here",bg="black",fg="white",font=("Arial",26,"bold"),command=myfun)
# command use for execute function
#btn.place(x=20,y=120)
# greed method
btn1 = tkinter.Button(screen,text="Call 1",font=("Arial",28,"bold"))
btn1.grid(row=0,column=0)
btn2 = tkinter.Button(screen,text="Call 2",font=("Arial",28,"bold"))
btn2.grid(row=0,column=1)
# to execute screen
screen.mainloop()


# calc_example
import tkinter
screen = tkinter.Tk()
screen.title("Calculator")
screen.geometry("300X300")
btn1 = tkinter.Button(screen,text="1",font=("Arial",18,"bold"))
btn1.grid(row=0,column=0)
btn2 = tkinter.Button(screen,text="1",font=("Arial",18,"bold"))
btn2.grid(row=0,column=1)


# calc
import tkinter
screen = tkinter.Tk()
screen.title("Calculator")
screen.geometry("300X300")
lbl = tkinter.Label(screen,text="Calculator",font=("Arial",22,"bold"))
lbl.pack()
btn1 = tkinter.Button(screen,text="1",font=("Arial",18,"bold"))
btn1.grid(row=0,column=0)
btn2 = tkinter.Button(screen,text="1",font=("Arial",18,"bold"))
btn2.grid(row=0,column=1)


# calculator example
import tkinter
screen = tkinter.Tk()
screen.title("Calculator")
screen.geometry("200x200")
btn1 = tkinter.Button(screen,text="1",font=("Arial",18,"bold"))
btn1.grid(row=0,column=0)
btn2 = tkinter.Button(screen,text="2",font=("Arial",18,"bold"))
btn2.grid(row=0,column=1)
btn3 = tkinter.Button(screen,text="3",font=("Arial",18,"bold"))
btn3.grid(row=0,column=2)
btn4 = tkinter.Button(screen,text="4",font=("Arial",18,"bold"))
btn4.grid(row=1,column=0)
btn5 = tkinter.Button(screen,text="5",font=("Arial",18,"bold"))
btn5.grid(row=1,column=1)
btn6 = tkinter.Button(screen,text="6",font=("Arial",18,"bold"))
btn6.grid(row=1,column=2)
btn7 = tkinter.Button(screen,text="7",font=("Arial",18,"bold"))
btn7.grid(row=2,column=0)
btn8 = tkinter.Button(screen,text="8",font=("Arial",18,"bold"))
btn8.grid(row=2,column=1)
btn9 = tkinter.Button(screen,text="9",font=("Arial",18,"bold"))
btn9.grid(row=2,column=2)
btn0 = tkinter.Button(screen,text="0",font=("Arial",18,"bold"))
btn0.grid(row=3,column=1)
screen.mainloop()