import random
from tkinter import *
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
word = {}
try:
    data = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("data/french_words.csv")
# words = {e.French: e.English for (f, e) in data.iterrows()}
words = data.to_dict(orient="records")


def to_eng():
    canvas.itemconfig(word_canvas, text=word["English"], fill="white")
    canvas.itemconfig(lang, text="English", fill="white")
    canvas.itemconfig(image, image=card_back)


def generate_word():
    global word, flip_timer
    window.after_cancel(flip_timer)
    word = random.choice(words)
    canvas.itemconfig(word_canvas, text=word["French"], fill="black")
    canvas.itemconfig(lang, text="French", fill="black")
    canvas.itemconfig(image, image=card_front)
    flip_timer = window.after(3000, func=to_eng)


def is_known():
    words.remove(word)
    print(len(words))
    new_data = pd.DataFrame(words)
    new_data.to_csv("data/words_to_learn.csv", index=False)
    generate_word()


window = Tk()
window.title("Flash cards")
window.config(bg=BACKGROUND_COLOR, pady=75, padx=75)
flip_timer = window.after(3000, func=to_eng)

tick_image = PhotoImage(file="./images/right.png")
wrong_image = PhotoImage(file="./images/wrong.png")
card_back = PhotoImage(file="./images/card_back.png")
card_front = PhotoImage(file="./images/card_front.png")

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
image = canvas.create_image(400, 263, image=card_front)
lang = canvas.create_text(400, 150, text="lang", font=("Arial", 40, "italic"))
word_canvas = canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

right_button = Button(image=tick_image, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=1)
wrong_button = Button(image=wrong_image, highlightthickness=0, command=generate_word)
wrong_button.grid(column=0, row=1)

generate_word()

window.mainloop()
