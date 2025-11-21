# Classical number guessing game
# the aim is to make gui interface for this game
# I want all numbers 1-100 to be shown
# add a field to enter number
# I want numbers to show which can and which cannot be right answers
# Add a leaderboard with points in toon maybe(?)
# two buttons one to enter number and one to show scores

# different approach. first cli based version then converting to gui with tkinter and then adding functionalities.

import random
import tkinter as tk
import csv

def random_number():
	return random.randint(1,100)
	
def points_count(num_of_tr):
    points=100
    for i in range(1,num_of_tr):
        points=points//2
    if points<5:
        return 5
    else:
        return points

class NumberGuessingGame:
    def __init__(self, window):
        self.window=window
        self.window.title("Number Guessing Game")
        self.window.rowconfigure(0, weight=1)
        self.window.columnconfigure(0, weight=1)
        self.window.columnconfigure(1, weight=1)
        self.solution=random_number()
        self.num_of_tr=1
        self.score=0
        self.numbers=[1]*100

        # Rules display
        Rules_text="You Have to guess number(1-100).\nWith every try points are being divided by 2.\n Lowest possible score is 5.\n Score is saved on the board.\nGood luck!"
        self.rules_label=tk.Label(window,text=Rules_text,width=100)
        self.rules_label.grid(row=0,column=0,columnspan=2)

        # Tiles helping with playing
        self.tiles_frame=tk.LabelFrame(window,text="Numbers", padx=10, pady=10)
        self.tiles_frame.grid(row=1,column=0)
        self.create_tiles(self.numbers)

        # Creating a guessing field with score information
        self.guess_field=tk.LabelFrame(window,text="guessing field",padx=10,pady=10)
        self.guess_field.grid(row=1,column=1)



    def create_tiles(self,numbers):
        for i in range(10):
            for j in range(10):
                num=(i*10+j+1)
                color="lightgreen" if numbers[(i*10+j)] else "red"
                self.tiles = tk.Label(self.tiles_frame,text=f"{num}",width=3,height=2,bg=f"{color}",fg="black")
                self.tiles.grid(row=i,column=j)
#    def update_tiles():
#    def chceck_guess():
#    def reset_game():

window = tk.Tk()
game = NumberGuessingGame(window)
window.mainloop()
'''
def game(solution):
    num_of_tr=1
    points=points_count(num_of_tr)
    score=0
    while True:                                     # guessing the number
        points=points_count(num_of_tr)
        answer=int(input(f"Guess the number({points} pts.): "))
        if answer>solution:
            print("Less.")
        elif answer<solution:
            print("More.")
        elif answer==solution:
            score=points
            return("Correct")
        num_of_tr+=1

# Done: 


# Not Done:
def tiles_shown(numbers):
    for i in range(10):
        for j in range(10):
            frame=tk.Frame(master=window,relief=tk.RAISED)
            frame.grid(row=i,column=j)
            tmp_num=(i+1)*(j+1)
            tmp_color="green"
            if numbers[(i+1)*(j+1)-1]:
                tmp_color="green"
            else:
                tmp_color="red"
            label = tk.Label(master=frame, text=f"{tmp_num}",width=5,height=3,bg=f"{tmp_color}",fg="black")
            label.pack()
            
            
#def saving_score():
#def loading_score():
def display_rules():
    return("Rules:\n You Have to guess the random number.\n With every try points are being divided by 2.\n Lowest possible score is 5.\n Score is saved on the board.\nGood luck!")

# Skeleton of game:  
window=tk.Tk()
window.title("Number Guessing Game") # changes window name

numbers=[1]*100
solution=random_number()

rules=tk.Label(text=display_rules())
rules.pack()
tiles_shown(numbers)
# Just trying out

game(solution)
window.mainloop()
'''