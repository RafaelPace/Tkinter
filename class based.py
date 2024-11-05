import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self, title, size):
        super().__init__()
        self.title('Class based app')
        self.geometry(f'{size[0]}x{size[1]}')
        self.minsize(size[0], size[1])

        self.mainloop()

App('Class based app', (600, 600))

