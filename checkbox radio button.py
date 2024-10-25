# https://youtu.be/mop6g-c5HEY 1:27:00

import tkinter as tk
from tkinter import ttk

# setup
window = tk.Tk()
window.title('buttons')
window.geometry('600x400')

# button
def button_func():
    print('a basic button')


button_string = tk.StringVar(value = 'a button with string var')
button = ttk.Button(window, text = 'A simple button', command = button_func, textvariable = button_string)
button.pack()

# checkbutton
check_var = tk.IntVar()
check = ttk.Checkbutton(window, text = 'checkbox 1', command = lambda: print(check_var.get()), variable = check_var, onvalue = 10, offvalue = 5)
check.pack()

# radio buttons
radio1 = ttk.Radiobutton(window, text = 'Radiobutton 1', value = 'radio 1', command = lambda: print("radio1 pressed"))
radio1.pack()
radio2 = ttk.Radiobutton(window, text = 'Radiobutton 2', value = 2)
radio2.pack()

# exercise
radio_string = tk.StringVar()
exercise_radio1 = ttk.Radiobutton(window, text = 'Radio A', value = 'A')
exercise_radio1.pack()
exercise_radio2 = ttk.Radiobutton(window, text = 'Radio B', value = 'B')
exercise_radio2.pack()
exercise_radio3 = ttk.Radiobutton(window, text = 'Radio C', value = 'C')
exercise_radio3.pack()

# run
window.mainloop()
