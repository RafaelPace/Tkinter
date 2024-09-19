# https://youtu.be/mop6g-c5HEY 37:00

import tkinter as tk
from tkinter import ttk

def button_func():
    print("button pressed")

def button2_func():
    print("Hello!!!!")

# create a window
window = tk.Tk()
window.title("Window and widgets")
window.geometry('1000x500')


# ttk label
label = ttk.Label(master = window, text = 'Teste!')
label.pack()

label2 = ttk.Label(master = window, text = 'Hello!')
label2.pack()

# create widgets
text = tk.Text(master = window)
text.pack()

# ttk entry
entry = ttk.Entry(master = window)
entry.pack()

# ttk button
button = ttk.Button(master = window, text = "Skirrrrr", command = button_func)
button.pack()

# new button
button2 = ttk.Button(master = window, text = "my label", command = button2_func)
button2.pack()


# run
window.mainloop()
