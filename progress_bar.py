import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

# window
window = tk.Tk()
window.title('sliders')
# slider
#scale_float = tk.DoubleVar(value = 15)
#scale = ttk.Scale(window, command = lambda value: progress.stop(),
#                   from_ = 0, to = 25, length = 300,
#                     orient = 'vertical', variable = scale_float)
#scale.pack()
# progress bar
#progress = ttk.Progressbar(window, variable = scale_float, maximum = 25, mode = 'determinate', length = 400)
#progress.pack()
# progress.start(500)
# scrolledtext
#scrolled_text = scrolledtext.ScrolledText(window, width = 40, height = 10)
#scrolled_text.pack()

labelnum = tk.IntVar(value = 0)
label = ttk.Label(window, textvariable = labelnum)
label.pack()

progress = ttk.Progressbar(window, variable = labelnum, maximum = 100, orient = 'vertical', length = 400)
progress.pack()
progress.start()

exercise_scale = ttk.Scale(window, variable = labelnum, from_ = 0, to = 100, length = 400)
exercise_scale.pack()

# run
window.mainloop()
