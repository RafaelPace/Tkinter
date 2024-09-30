import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk
from tkinter import colorchooser

brush_size = 5
color = 'black'

if brush_size < 0:
    brush_size = 1

def color_func():
    global color
    chosen_color = colorchooser.askcolor()[1]
    if chosen_color:
        color = chosen_color 

def upsize_func():
    global brush_size
    brush_size += 10
    size.config(text=f'size: {brush_size}') 

def downsize_func():
    global brush_size
    brush_size -= 10
    if brush_size < 1:
        brush_size = 1
    size.config(text=f'size: {brush_size}') 
    
def black_func():
    global color
    color = 'black'

def brown_func():
    global color
    color = 'brown'

def red_func():
    global color
    color = 'red'

def green_func():
    global color
    color = 'green'

def blue_func():
    global color
    color = 'blue'

def white_func():
    global color
    color = 'white'

def lblue_func():
    global color
    color = 'light blue'

def yellow_func():
    global color
    color = 'yellow'

def draw_on_canvas(event):
    x = event.x
    y = event.y
    canvas.create_oval(x - brush_size / 2, y - brush_size / 2, x + brush_size / 2, y + brush_size / 2, 
                       width=0, outline=color, fill=color)

def brush_size_adjust(event):
    global brush_size
    if event.delta > 0:
        brush_size += 4
    else:
        brush_size -= 4
    if brush_size <= 0:
        brush_size = 1
    size.config(text=f'size: {brush_size}')

# setup
window = tk.Tk()
window.geometry('800x600')
window.title('Canvas') 

# Canvas

size = tk.Label(window, text=f'size: {brush_size}', font='ventura 16 bold')
size.pack() 

canvas = tk.Canvas(window, bg='white', width=600, height=400)
canvas.pack()
canvas.bind('<B1-Motion>', draw_on_canvas)
canvas.bind('<MouseWheel>', brush_size_adjust)

# Brush size buttons
button1 = tk.Button(window, text='size up', command=upsize_func)
button1.place(x=730, y=100)

button2 = tk.Button(window, text='size down', command=downsize_func)
button2.place(x=730, y=120)

# Color buttons
butgreen = tk.Button(window, text=' ', bg='green', command=green_func, width=2)
butgreen.place(x=100, y=450)

butred = tk.Button(window, text=' ', bg='red', command=red_func, width=2)
butred.place(x=120, y=450)

butblack = tk.Button(window, text=' ', bg='black', command=black_func, width=2)
butblack.place(x=140, y=450)

butblue = tk.Button(window, text=' ', bg='blue', command=blue_func, width=2)
butblue.place(x=160, y=450)

butlightblue = tk.Button(window, text=' ', bg='light blue', command=lblue_func, width=2)
butlightblue.place(x=180, y=450)

butyellow = tk.Button(window, text=' ', bg='yellow', command=yellow_func, width=2)
butyellow.place(x=200, y=450)

butcolor = tk.Button(window, text='choose color', bg='white', command=color_func)
butcolor.place(x=220, y=450)

butwhite = tk.Button(window, text='eraser', bg='white', command=white_func)
butwhite.place(x=300, y=450)

# run
window.mainloop()
