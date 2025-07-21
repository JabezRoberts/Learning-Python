from tkinter import *
from tkinter import messagebox
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

current_card = {}
to_learn={}


try:
    word_bank = pandas.read_csv("C:/Users/Zeilhan Co/Desktop/Study/100 Days of Code Python/Code/Day 31 - Intermediate CAPSTONE Flash Card App/Start/data/Words I've Learned.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("C:/Users/Zeilhan Co/Desktop/Study/100 Days of Code Python/Code/Day 31 - Intermediate CAPSTONE Flash Card App/Start/data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = word_bank.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    
    current_card = random.choice(to_learn)
    
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(study_word, text=current_card["French"], fill='black')
    canvas.itemconfig(card_background, image=card_front_image)
    
    flip_timer = window.after(3000, func=flip_card)
    

def flip_card():
    canvas.itemconfig(card_title, text="English", fill='white')
    canvas.itemconfig(study_word, text=current_card["English"], fill='white')
    canvas.itemconfig(card_background, image=card_back_image)
    window.after(3000, func=flip_card)


def word_known():
    to_learn.remove(current_card)
    
    learned_words = pandas.DataFrame(to_learn)
    learned_words.to_csv("C:/Users/Zeilhan Co/Desktop/Study/100 Days of Code Python/Code/Day 31 - Intermediate CAPSTONE Flash Card App/Start/data/Words I've Learned.csv", index=FALSE)
    
    next_card()


window = Tk()
window.title("CAPSTONE FLASH CARD APP")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file="C:/Users/Zeilhan Co/Desktop/Study/100 Days of Code Python/Code/Day 31 - Intermediate CAPSTONE Flash Card App/Start/images/card_front.png")
card_back_image = PhotoImage(file="C:/Users/Zeilhan Co/Desktop/Study/100 Days of Code Python/Code/Day 31 - Intermediate CAPSTONE Flash Card App/Start/images/card_back.png")

card_background = canvas.create_image(400, 236, image=card_front_image)

card_title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
study_word = canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))


canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)


wrong_image = PhotoImage(file="C:/Users/Zeilhan Co/Desktop/Study/100 Days of Code Python/Code/Day 31 - Intermediate CAPSTONE Flash Card App/Start/images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

right_image = PhotoImage(file="C:/Users/Zeilhan Co/Desktop/Study/100 Days of Code Python/Code//Day 31 - Intermediate CAPSTONE Flash Card App/Start/images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=word_known)
right_button.grid(row=1,column=1)



next_card()

window.mainloop()