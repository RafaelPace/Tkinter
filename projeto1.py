# https://youtu.be/mop6g-c5HEY 18:00

import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    pounds_input = entry_int.get()
    kg_output = pounds_input * 0.453592
    output_string.set(kg_output)

# window
window = ttk.Window(themename = 'darkly')
window.title("Lbs to Kg")
window.geometry('500x250')

# title
title_label = ttk.Label(master = window, text = 'Pounds to Kg', font = 'Ventura 32 bold')
title_label.pack()

# input field
input_frame = ttk.Frame(master = window)
entry_int = tk.IntVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)
button = ttk.Button(master = input_frame, text = "Convert", command = convert)
entry.pack(side = 'left')
button.pack(side = 'left')
input_frame.pack(pady = 50)

#output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Ventura 24', textvariable = output_string)
output_label.pack()

# run
window.mainloop()

