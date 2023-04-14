import tkinter as tk
import random

# Defining the root 
root = tk.Tk()
root.title("Rock Paper Scissor")

# Define variables for user and computer score
user_score = 0
computer_score = 0

# Define a function to update the score and result
def update_score(result):
    global user_score, computer_score
    if result == "User":
        user_score += 1
    elif result == "Computer":
        computer_score += 1
    user_score_label.config(text="USER: {}".format(user_score))
    computer_score_label.config(text="COMPUTER: {}".format(computer_score))
    result_label.config(text=result)

# Define a function for the user's choice
def user_choice(choice):
    computer_choice = random.choice(["Rock", "Paper", "Scissor"])
    if choice == "Rock":
        if computer_choice == "Rock":
            update_score("Tie")
        elif computer_choice == "Paper":
            update_score("Computer")
        else:
            update_score("User")
    elif choice == "Paper":
        if computer_choice == "Rock":
            update_score("User")
        elif computer_choice == "Paper":
            update_score("Tie")
        else:
            update_score("Computer")
    else:
        if computer_choice == "Rock":
            update_score("Computer")
        elif computer_choice == "Paper":
            update_score("User")
        else:
            update_score("Tie")

# Define the user interface
rock_button = tk.Button(root, text="ROCK", width=15, height=5, command=lambda: user_choice("Rock"))
paper_button = tk.Button(root, text="PAPER", width=15, height=5, command=lambda: user_choice("Paper"))
scissors_button = tk.Button(root, text="SCISSOR", width=15, height=5, command=lambda: user_choice("Scissor"))
rock_button.grid(row=0, column=0)
paper_button.grid(row=0, column=1)
scissors_button.grid(row=0, column=2)

user_score_label = tk.Label(root, text="USER: 0")
computer_score_label = tk.Label(root, text="COMPUTER: 0")
user_score_label.grid(row=1, column=0, columnspan=2)
computer_score_label.grid(row=1, column=1, columnspan=2)

result_label = tk.Label(root, text="RESULT", font=("Arial", 24))
result_label.grid(row=2, column=0, columnspan=3)

root.mainloop()
