import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

brush_size = 5
color = 'black'

if brush_size < 0:
    brush_size = 1

def upsize_func():
    global brush_size
    brush_size += 10

def downsize_func():
    global brush_size
    brush_size -= 10
    if brush_size < 0:
        brush_size = 1
    
def black_func():
    global color
    color = 'black'

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


def draw_on_canvas(event):
    x = event.x
    y = event.y
    canvas.create_oval(x, y, x, y, width = brush_size, outline = color)

# setup
window = tk.Tk()
window.geometry('800x600')
window.title('Canvas') 


# Canvas
canvas = tk.Canvas(window, bg = 'white', width=600, height=400)
canvas.pack()
canvas.bind('<B1-Motion>', draw_on_canvas)

button1 = tk.Button(window, text = '   sizeup  ', command = upsize_func)
button1.place(x=730, y=100)

button2 = tk.Button(window, text = 'sizedown', command = downsize_func)
button2.place(x=730, y=120)


butgreen = tk.Button(window, text = '   ', bg = 'green', command = green_func)
butgreen.pack()

butred = tk.Button(window, text = '   ', bg = 'red', command = red_func)
butred.pack()

butblack = tk.Button(window, text = '   ', bg = 'black', command = black_func)
butblack.pack()

butblue = tk.Button(window, text = '   ', bg = 'blue', command = blue_func)
butblue.pack()

butwhite = tk.Button(window, text = 'eraser', bg = 'white', command = white_func)
butwhite.pack()

# run
window.mainloop()
