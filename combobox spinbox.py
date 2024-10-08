import tkinter as tk
from tkinter import ttk

# setup
window = tk.Tk()
window.geometry('600x400')
window.title("Combo and Spin")

# Combobox
items = ('Ice cream', 'Pizza', 'Chocolate')
food_string = tk.StringVar(value = items[0])
combo = ttk.Combobox(window, textvariable = food_string)
combo['values'] = items
combo.pack()

# events
combo.bind('<<ComboboxSelected>>', lambda event: combo_label.config(text = f'Selected value: {food_string.get()}'))

combo_label = ttk.Label(window, text = 'a label')
combo_label.pack()

# Spinbox
#spin_int = tk.IntVar(value = 12)
#spin = ttk.Spinbox(window, from_ = 3, to = 20, command = lambda: print('an arrow was pressed'), textvariable = spin_int)
#spin.bind('<<Increment>>', lambda event: print('arrowup'))
# spin['value'] = (1, 2, 3, 4, 5)
# spin.pack()

# Exercise
spin = ttk.Spinbox(window, )
spin['value'] = ('A', 'B', 'C', 'D', 'E')
spin.bind('<<Decrement>>', lambda event:print(spin.get()))
spin.pack()

# run
window.mainloop()
