import random
import tkinter
from tkinter import PhotoImage
import pandas

current_card = {}
toLearn = {}

try:
    data  = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
else:
    toLearn = data.to_dict(orient="records")



def next_card ():
    global current_card , flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(toLearn)
    canvas.itemconfig(card_title,text="French")
    canvas.itemconfig(card_word,text=current_card["French"])
    canvas.itemconfig(c_image, image=front_flip)
    flip_timer = window.after(3000,func=eng_card)


def eng_card():
    global current_card
    canvas.itemconfig(c_image,image = back_flip)
    canvas.itemconfig(card_title,text="English")
    canvas.itemconfig(card_word, text=current_card["English"])

def remove_card():
    toLearn.remove(current_card)
    data = pandas.DataFrame(toLearn)
    data.to_csv("data/words_to_learn.csv",index=False)
    next_card()



BACKGROUND_COLOR = "#B1DDC6"

window =tkinter.Tk()
window.config(pady=50,padx=50,bg=BACKGROUND_COLOR)
window.title("Flip card")
flip_timer = window.after(3000,func=eng_card)


canvas = tkinter.Canvas(width=800,height=526 , bg=BACKGROUND_COLOR , highlightthickness=0)
front_flip = PhotoImage(file="images/card_front.png")
back_flip = PhotoImage(file="images/card_back.png")
c_image = canvas.create_image(400,263,image =front_flip)
card_title = canvas.create_text(400,150,text="Title",font=("Ariel",24,"italic"))
card_word = canvas.create_text(400,250,text="Word",font=("Ariel",40,"italic"))
canvas.grid(row=0,column=0,columnspan =2)

cross_img = PhotoImage(file="images/wrong.png")
red_button = tkinter.Button(image=cross_img,highlightthickness=0 , command=next_card)
red_button.grid(row=1,column=0)

cross_img1 = PhotoImage(file="images/right.png")
green_button = tkinter.Button(image=cross_img1,highlightthickness=0,command=remove_card)
green_button.grid(row=1,column=1)


next_card()

window.mainloop()
