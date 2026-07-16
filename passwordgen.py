import string
import random
import tkinter as tk


def create(event):
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation
    question = int(info.get())

    populations = letters + numbers + symbols
    choice = random.choices(population=populations, k=question)
    joined = "".join(choice)
    lable = tk.Label(window, text=joined)
    lable.pack()


window = tk.Tk()
window.geometry("500x200")
window.title("Password generator")

text1 = tk.Label(window, text="Choose how many characters you want")
text1.pack()

info = tk.Entry(window, width=25)
info.pack()

info.bind('<Return>', func=create)




window.mainloop()