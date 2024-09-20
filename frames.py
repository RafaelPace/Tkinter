import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.geometry("600x400")
window.title('Frames and parenting')

# frame
frame = ttk.Frame(window, width = 100, height = 200, borderwidth = 10, relief = tk.GROOVE)
frame.pack_propagate(False)
frame.pack(side = 'left')


# master setting
label = ttk.Label(frame, text = 'label in frame')
label.pack()

button = ttk.Button(frame, text = 'button in a frame')
button.pack()

# example
label2 = ttk.Label(window, text = 'Label outside frame')
label2.pack(side = 'left')

frame2 = ttk.Frame(window, width = 100, height = 200, borderwidth = 10, relief = tk.GROOVE)
frame2.pack_propagate
frame2.pack(side = 'right')

button2 = ttk.Button(frame2, text = 'button in the right')
button2.pack(side = 'right')

label3 = ttk.Label(frame2, text = 'label in frame2')
label3.pack(side = 'right')


# run
window.mainloop()

