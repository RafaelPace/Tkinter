# https://youtu.be/mop6g-c5HEY 54:00

import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk
import math

def button1_func():
    number = int(entry.get())
    print(math.sqrt(number))
    label.config(text = math.sqrt(number))

def button2_func():
    label.configure(text = "raiz")

# window
window = ttk.Window(themename = 'darkly')
window.title("Getting and setting widgets")
window.geometry('300x250')

# widgets
label = ttk.Label(master = window, text = "raiz", font = "Arial 25 bold")
label.pack()

entry = ttk.Entry(master = window) 
entry.pack()

button1 = ttk.Button(master = window, text = "Raiz quadrada", command = button1_func)
button1.pack()
button1.pack(pady = 10)

button2 = ttk.Button(master = window, text = "Reset!", command = button2_func)
button2.pack()


# run
window.mainloop()