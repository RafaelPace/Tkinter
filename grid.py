import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('grid')
window.geometry('600x400')

# widgets
label1 = ttk.Label(window, text = 'Label 1', background = 'red')
label2 = ttk.Label(window, text = 'Label 2', background = 'blue')
label3 = ttk.Label(window, text = 'Label 3', background = 'green')
label4 = ttk.Label(window, text = 'Label 4', background = 'yellow')
button1 = ttk.Button(window, text = 'Button 1')
button2 = ttk.Button(window, text = 'Button 2')

# define a grid
window.columnconfigure((0, 1, 2), weight = 1)
window.columnconfigure(1, weight = 1)
window.columnconfigure(2, weight = 1)
window.columnconfigure(3, weight = 10)
window.rowconfigure(0, weight = 1)
window.rowconfigure(1, weight = 1)
window.rowconfigure(2, weight = 1)
window.rowconfigure(3, weight = 3)

# place a widget
label1.grid(row = 0, column = 0, sticky = 'nsew')
label2.grid(row = 1, column = 1, rowspan = 3, sticky = 'nsew')
label3.grid(row = 1, column = 3, sticky = 'nsew', padx = 20, pady = 10)
label4.grid(row = 3, column = 3, sticky = 'se')

# run
window.mainloop()
