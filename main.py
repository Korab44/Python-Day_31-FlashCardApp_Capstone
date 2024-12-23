from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"



data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")
current_card = {}



def randomFrench():
    canvas.itemconfig(image, image=front_pic)
    global current_card, flip_timer
    screen.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    flip_timer = screen.after(3000, change)
def change():
    canvas.itemconfig(image, image=back_pic)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
screen = Tk()
screen.title("Flash Card App")
screen.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = screen.after(3000, change)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_pic = PhotoImage(file="images/card_front.png")
back_pic = PhotoImage(file="images/card_back.png")
image = canvas.create_image(400, 263, image=front_pic)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)



wrong_image = PhotoImage(file="images/wrong.png")
wrong_btn = Button(image=wrong_image, highlightthickness=0, command=randomFrench)
wrong_btn.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
right_btn = Button(image=right_image, highlightthickness=0, command=randomFrench)
right_btn.grid(row=1, column=1)

randomFrench()

screen.mainloop()



