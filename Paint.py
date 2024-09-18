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
    size.config(text=f'size: {brush_size}') 

def downsize_func():
    global brush_size
    brush_size -= 10
    if brush_size < 0:
        brush_size = 1
    size.config(text=f'size: {brush_size}') 
    
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

def lblue_func():
    global color
    color = 'sky blue'

def yellow_func():
    global color
    color = 'yellow'


def draw_on_canvas(event):
    x = event.x
    y = event.y
    canvas.create_oval(x, y, x, y, width = brush_size, outline = color, fill = color)

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

size = tk.Label(window, text = f'size: {brush_size}', font = 'ventura 16 bold')
size.pack() 


canvas = tk.Canvas(window, bg = 'white', width=600, height=400)
canvas.pack()
canvas.bind('<B1-Motion>', draw_on_canvas)
canvas.bind('<MouseWheel>', brush_size_adjust)

button1 = tk.Button(window, text = '   sizeup  ', command = upsize_func)
button1.place(x=730, y=100)

button2 = tk.Button(window, text = 'sizedown', command = downsize_func)
button2.place(x=730, y=120)


butgreen = tk.Button(window, text = '   ', bg = 'green', command = green_func)
butgreen.place(x = 100, y = 450)

butred = tk.Button(window, text = '   ', bg = 'red', command = red_func)
butred.place(x = 120, y = 450)

butblack = tk.Button(window, text = '   ', bg = 'black', command = black_func)
butblack.place(x = 140, y = 450)

butblue = tk.Button(window, text = '   ', bg = 'blue', command = blue_func)
butblue.place(x = 160, y = 450)

butlightblue = tk.Button(window, text = '   ', bg = 'sky blue', command = lblue_func)
butlightblue.place(x = 180, y = 450)

butyellow = tk.Button(window, text = '   ', bg = 'yellow', command = yellow_func)
butyellow.place(x = 200, y = 450)

butwhite = tk.Button(window, text = 'eraser', bg = 'white', command = white_func)
butwhite.place(x = 220, y = 450)

# run
window.mainloop()
