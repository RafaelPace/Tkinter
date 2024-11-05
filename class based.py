import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self, title, size):
        super().__init__()
        self.title(title)
        self.geometry(f'{size[0]}x{size[1]}')
        self.minsize(size[0], size[1])

        # Initialize layout
        self.create_widgets()
        
    def create_widgets(self):
        # Main layout widgets
        self.menu_frame = ttk.Frame(self)
        self.main_frame = ttk.Frame(self)

        # Main place layout
        self.menu_frame.place(x=0, y=0, relwidth=0.3, relheight=1)
        self.main_frame.place(relx=0.3, y=0, relwidth=0.7, relheight=1)

        # Menu widgets
        self.menu_button1 = ttk.Button(self.menu_frame, text='Button1')
        self.menu_button2 = ttk.Button(self.menu_frame, text='Button2')
        self.menu_button3 = ttk.Button(self.menu_frame, text='Button3')

        self.menu_slider1 = ttk.Scale(self.menu_frame, orient='vertical')
        self.menu_slider2 = ttk.Scale(self.menu_frame, orient='vertical')

        self.toggle_frame = ttk.Frame(self.menu_frame)
        self.menu_toggle1 = ttk.Checkbutton(self.toggle_frame, text='check 1')
        self.menu_toggle2 = ttk.Checkbutton(self.toggle_frame, text='check 2')

        self.entry = ttk.Entry(self.menu_frame)

        # Menu layout
        self.menu_frame.columnconfigure((0, 1, 2), weight=1, uniform='a')
        self.menu_frame.rowconfigure((0, 1, 2, 3, 4), weight=1, uniform=1)

        self.menu_button1.grid(row=0, column=0, sticky='nsew', columnspan=2)
        self.menu_button2.grid(row=0, column=2, sticky='nsew')
        self.menu_button3.grid(row=1, column=0, sticky='nsew', columnspan=3)

        self.menu_slider1.grid(row=2, column=0, rowspan=2, sticky='nsew', pady=30)
        self.menu_slider2.grid(row=2, column=2, rowspan=2, sticky='nsew', pady=30)

        # Toggle layout
        self.toggle_frame.grid(row=4, column=0, columnspan=3, sticky='nsew')
        self.menu_toggle1.pack(side='left', expand=True)
        self.menu_toggle2.pack(side='left', expand=True)

        # Entry layout
        self.entry.place(relx=0.5, rely=0.95, relwidth=0.9, anchor='center')

        # Main frame widgets
        self.entry_frame1 = ttk.Frame(self.main_frame)
        self.main_label1 = ttk.Label(self.entry_frame1, text='label1', background='red')
        self.main_button1 = ttk.Button(self.entry_frame1, text='Button 1')

        self.entry_frame2 = ttk.Frame(self.main_frame)
        self.main_label2 = ttk.Label(self.entry_frame2, text='label2', background='blue')
        self.main_button2 = ttk.Button(self.entry_frame2, text='Button 2')

        # Main frame layout
        self.entry_frame1.pack(side='left', expand=True, fill='both', padx=20, pady=20)
        self.entry_frame2.pack(side='left', expand=True, fill='both', padx=20, pady=20)

        self.main_label1.pack(expand=True, fill='both')
        self.main_button1.pack(expand=True, fill='both', pady=10)

        self.main_label2.pack(expand=True
