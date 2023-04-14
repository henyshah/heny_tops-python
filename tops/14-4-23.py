import random
import tkinter
# take the base screen
screen = tkinter.Tk()
# screen geometry
screen.geometry("400x400")


# logic implementation
l1=["ROCK","PAPER","SCISSOR"]
def mygame(userchoice):
    print(userchoice)
    computerChoice=random.choice(l1)
    if userchoice==computerChoice:
        print("TIE")

# display label
lbl = tkinter.Label(screen,text="Rock Paper Scissor",font=("Arial",22,"bold"))
lbl.pack()

# begin rock paper and scissor button
e1 = tkinter.Button(screen,text="Rock",bg="blue",fg="white",font=("Arial",18,"bold"),command=lambda:mygame("ROCK"))
e1.place(x=50,y=80)

e2 = tkinter.Button(screen,text="Paper",bg="blue",fg="white",font=("Arial",18,"bold"),command=lambda:mygame("PAPER"))
e2.place(x=150,y=80)

e3 = tkinter.Button(screen,text="Scissor",bg="blue",fg="white",font=("Arial",18,"bold"),command=lambda:mygame("SCISSOR"))
e3.place(x=250,y=80)
# end rock,paper,scissor button

# begin user score board
e4 = tkinter.Label(screen,text="User",font=("Arial",14,"bold"))
e4.place(x=50,y=180)

e5 = tkinter.Label(screen,text="0",font=("Arial",14,"bold"))
e5.place(x=130,y=180)

e6 = tkinter.Label(screen,text="Computer",font=("Arial",14,"bold"))
e6.place(x=200,y=180)

e7 = tkinter.Label(screen,text="0",font=("Arial",14,"bold"))
e7.place(x=320,y=180)
# end user score board

e8 = tkinter.Button(screen,text="Result",bg="lightblue",fg="white",font=("Arial",20,"bold"),width=13,height=1)
e8.place(x=100,y=290)

screen.mainloop()