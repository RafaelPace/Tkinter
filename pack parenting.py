import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('pack parenting')
window.geometry('400x600')

# Top frame
top_frame = ttk.Frame(window)
label1 = ttk.Label(top_frame, text = 'first label', background = 'red')
label2 = ttk.Label(top_frame, text = 'label 2', background = 'blue')


# midle widget
label3 = ttk.Label(window, text = 'Another label', background = 'green')

# bottom frame
bottom_frame = ttk.Frame(window)
label4 = ttk.Label(bottom_frame, text = 'Last of the labels', background = 'orange')
button = ttk.Button(bottom_frame, text = 'A Button')
button2 = ttk.Button(bottom_frame, text = 'Another Button')

# top layout
label1.pack(fill = 'both', expand = True)
label2.pack(fill = 'both', expand = True)
top_frame.pack(fill = 'both', expand = True)

# middle layout
label3.pack(expand = True)

# bottom layout
button.pack(side = 'left', expand = True, fill = 'both')
label4.pack(side = 'left', expand = True, fill = 'both')
button2.pack(side = 'left', expand = True, fill = 'both')
bottom_frame.pack(expand = True, fill = 'both')

# run
window.mainloop()
