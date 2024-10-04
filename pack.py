import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('pack')
window.geometry('600x400')

# widgets
label1 = ttk.Label(window, text = 'first label', background = 'red')
label2 = ttk.Label(window, text = 'label 2', background = 'blue')
label3 = ttk.Label(window, text = 'Last of the labels', background = 'green')
button = ttk.Button(window, text = 'Button')

# layout
label1.pack(side = 'top', expand = True, fill = 'both', ipady = 50, ipadx = 100)
label2.pack(side = 'right', expand = True, fill = 'both')
label3.pack(side = 'top')
button.pack(side = 'top', expand = True, fill = 'both')

# run
window.mainloop()
