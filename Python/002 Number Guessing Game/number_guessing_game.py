# Classical number guessing game
# the aim is to make gui interface for this game
# I want all numbers 1-100 to be shown
# add a field to enter number
# I want numbers to show which can and which cannot be right answers
# Add a leaderboard with points in toon maybe(?)
# two buttons one to enter number and one to show scores

# different approach. first cli based version then converting to gui with tkinter and then adding functionalities.

# dont work properly right now but i'm still working on backend. frontend is almost ready

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
        self.solution=random_number()
        self.num_of_tr=1
        self.score=0
        self.numbers=[1]*100
        self.guess=0

        # Rules display
        Rules_text="You Have to guess number(1-100).\nWith every try points are being divided by 2.\n Lowest possible score is 5.\n Score is saved on the board.\nGood luck!"
        self.rules_label=tk.Label(window,text=Rules_text)
        self.rules_label.grid(column=0,row=0,columnspan=2)

        # Tiles helping with playing
        self.tiles_frame=tk.LabelFrame(window,text="Numbers", padx=10, pady=10)
        self.tiles_frame.grid(column=0,row=1)
        self.create_tiles()

        # Creating a guessing field with score information
        self.guess_frame=tk.LabelFrame(window,text="Guess", padx=10, pady=10)
        self.guess_frame.grid(column=1,row=1)
        self.enter_guess()

        # Checking if solution==guess
        self.update_tiles()
        #self.create_tiles()
    def create_tiles(self):
        for i in range(10):
            for j in range(10):
                num=(i*10+j+1)
                color="lightgreen" if self.numbers[(i*10+j)] else "red"
                self.tiles = tk.Label(self.tiles_frame,text=f"{num}",width=3,height=2,bg=f"{color}",fg="black")
                self.tiles.grid(row=i,column=j)

    def update_tiles(self):
        if self.solution<int(self.guess):            # if lower 
            self.num_of_tr+=1
            for i in range (self.guess,100):
                self.numbers[i]=0
            self.create_tiles()
        elif int(self.guess)<self.solution:           # if more
            self.num_of_tr+=1
            for i in range (0,self.guess):
                self.numbers[i]=0
            self.create_tiles()
        elif int(self.guess)==self.solution:            # equal
            self.num_of_tr=1
            score=points_count(num_of_tr)

    
    def enter_guess(self):
        self.content=tk.Frame(self.guess_frame,pady=10,padx=10)
        self.guess_entry=tk.Entry(self.content,width=30)
        self.guess_entry.grid(row=0,column=0)
        self.points=tk.Label(self.content, text=f"You can get {points_count(self.num_of_tr)} for correct answer.")
        self.button=tk.Button(self.content,text="Submit.")
        self.button.grid(column=0,row=1)
        self.points.grid(row=2,column=0)
        self.content.grid(column=0,row=0)

#    def save_game():

window = tk.Tk()
game = NumberGuessingGame(window)
window.mainloop()