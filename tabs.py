import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry('600x400')
window.title('tab widget')

# Notebook widget
notebook = ttk.Notebook(window)

# tab 1
tab1 = ttk.Frame(notebook)
label1 = ttk.Label(tab1, text = 'text in tab1')
label1.pack()
button1 = ttk.Button(tab1, text = 'button in tab1')
button1.pack()

# tab 2
tab2 = ttk.Frame(notebook)
label2 = ttk.Label(tab2, text = 'text in tab2')
label2.pack()
entry2 = ttk.Entry(tab2)
entry2.pack()

# tab 3
tab3 = ttk.Frame(notebook)
label3 = ttk.Label(tab3, text = 'text in tab3')
label3.pack()
button3 = ttk.Button(tab3, text = 'button in tab3')
button3.pack()
button4 = ttk.Button(tab3, text = 'button in tab3')
button4.pack()

# Add tabs to notebook
notebook.add(tab1, text = 'tab 1')
notebook.add(tab2, text = 'tab 2')
notebook.add(tab3, text = 'tab 3')

# Pack the notebook
notebook.pack(expand=1, fill='both')

# run
window.mainloop()
