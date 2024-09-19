import tkinter as tk
from tkinter import ttk

brush_size = 5

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


def draw_on_canvas(event):
    x = event.x
    y = event.y
    canvas.create_oval(x, y, x, y, width = brush_size)

# setup
window = tk.Tk()
window.geometry('600x400')
window.title('Canvas') 

# Canvas
canvas = tk.Canvas(window, bg = 'white')
canvas.pack()
canvas.bind('<Motion>', draw_on_canvas)

button1 = tk.Button(window, text = 'sizeup', command = upsize_func)
button1.pack()

button2 = tk.Button(window, text = 'sizedown', command = downsize_func)
button2.pack()

# run
window.mainloop()



#canvas.create_rectangle((50, 20, 100, 200), fill = 'purple', width = 10, dash = (100, 2,3, 2, 15), outline = 'green')
#canvas.create_oval(300, 300, 100, 50)
#canvas.create_arc((300, 300, 100, 50), fill = 'red', start = '45', style = tk.ARC, outline = 'yellow', width = 10)
#canvas.create_line((300, 100, 100, 200), fill = 'blue')
#canvas.create_polygon((0, 0, 100, 200, 300, 50, 600, 100, 110, 100), fill = 'grey')
#canvas.create_text((175,125,), text = 'this is some text', fill = 'green', width = 20)
#canvas.create_window((100, 100), window = ttk.Button(window, text=' this is a button in a canvas '))
