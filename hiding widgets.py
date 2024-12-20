import tkinter as tk
from tkinter import ttk

# setup
window = tk.Tk()
window.geometry('600x400')
window.title('Hide widgets')

# place
# def toggle_label_place():
#     global label_visible
#     if label_visible:
#         label.place_forget()
#         label_visible = False
#     else:
#         label.place(relx = 0.5, rely = 0.5, anchor = 'center')
#         label_visible = True

# button = ttk.Button(window, text = 'toggle Label', command = toggle_label_place)
# button.place(x = 10, y = 10)

# label_visible = True
# label = ttk.Label(window, text = 'A label', background = 'green')
# label.place(relx = 0.5, rely = 0.5, anchor = 'center')

# grid
def toggle_label_grid():
    global label_visible
    if label_visible:
        label.grid_forget()
        label_visible = False
    else:
        label.grid(column = 1, row = 0)
        label_visible = True

window.columnconfigure((0,1), weight = 1, uniform='a')
window.rowconfigure(0, weight = 1, uniform='a')

button = ttk.Button(window, text = 'toggle Label', command = toggle_label_grid)
button.grid(column = 0, row = 0)

label_visible = True
label = ttk.Label(window, text = 'A label')
label.grid(column = 1, row = 0)

# run
window.mainloop()
