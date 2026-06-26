import random
from tkinter import *

window = Tk()
window.title('Guess A Number')
window.geometry('400x300')

num=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


entry =Entry(window)
entry.pack()

result =Label(window,
            text=""
           )
result.pack()

label = Label(window, text='Enter a number')
label.pack()

def play():
    user_choice = int(entry.get())
    computer_choices = random.choice(num)

    if(user_choice == computer_choices):
        result.config(text=f"YOU WIN")
        print('YOU WIN')
    else:
        result.config(text=f"YOU LOOSE")
        print('YOU LOSE')
        
button = Button(window, 
                   text='Submit', 
                   command=play
                )
button.pack()

window.mainloop()