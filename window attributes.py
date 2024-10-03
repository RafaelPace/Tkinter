import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('more on the window')
window.iconbitmap('money.ico')

# exercise

window.geometry(f'600x400+{int(window.winfo_screenwidth() // 2 - 300)}+{int(window.winfo_screenheight() // 2 - 200)}')

# window sizes
window.minsize(200, 400)
# window.resizable(True, False)

# screen attributes
print(window.winfo_screenwidth())
print(window.winfo_screenheight())

# window attributes
window.attributes('-alpha', 1)
window.attributes('-topmost', True)

# security event
window.bind('<Escape>', lambda e: window.quit())

# window.attributes('-disable', False)
# window.attributes('-fullscreen', False)

# title bar
window.overrideredirect(True)
grip = ttk.Sizegrip(window)
grip.place(relx = 1.0, rely = 1.0, anchor = 'se')

# run
window.mainloop()
