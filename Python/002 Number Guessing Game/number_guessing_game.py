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
        self.points=points_count(self.num_of_tr)
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
        # Entry Frame
        self.content=tk.Frame(self.guess_frame,pady=10,padx=10)
        # Entry
        self.guess_entry=tk.Entry(self.content,width=30)
        self.guess_entry.grid(row=1,column=0)
        self.guess_entry.bind('<Return>', lambda e:self.update_tiles())
        # Button
        self.button=tk.Button(self.content,text="Submit.",command=self.update_tiles)
        self.feedback_label=tk.Label(self.content,text="Please, enter a number", pady=10,padx=10)
        self.points_label=tk.Label(self.content, text=f"You can get {self.points} for correct answer.")
        self.feedback_label.grid(column=0,row=0)
        self.content.grid(column=0,row=2)
        self.button.grid(column=0,row=3)
        self.points_label.grid(row=4,column=0)

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
        try:
            self.guess=int(self.guess_entry.get())
            self.num_of_tr+=1
            # Check if number is correct
            if self.guess<1 or 100<self.guess:
                self.feedback_label.config(text="Please correct number(1-100).")
                return
            # If solution is lower than guess
            elif self.solution<int(self.guess):
                self.feedback_label.config(text="Less.")
                for i in range (self.guess,100):
                    self.numbers[i]=0
                self.create_tiles()
            # If guess is lower than solution
            elif int(self.guess)<self.solution:
                for i in range (0,self.guess):
                    self.numbers[i]=0
                self.create_tiles()
            # If guessed
            elif int(self.guess)==self.solution:
                self.score=points_count(self.num_of_tr)
            self.points=points_count(self.num_of_tr)
            self.points_label.config(text=f"You can get {self.points} for correct answer.")
            
        # If not number entered
        except ValueError:
            pass

#    def save_game():

window = tk.Tk()
game = NumberGuessingGame(window)
window.mainloop()