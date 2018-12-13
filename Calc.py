import tkinter as tk

window = tk.Tk()
window.mainloop()

window.title('Calculator;')

hello_world = tk.Label(window, text='Hello, World!')
hello_world.pack()

button1 = tk.Button(winodw, text='Button')
button1.pack()

input = tk.Entry(window, width=10)
input.pack()

from thkinter import ttk
combolist = ttk.Combobox(window, width=20, state'readonly')
combolist.pack()

from tkinter import scrolldtext

multi_text = srolledtext.ScrolldeText(window, width=30, height=5, wrap=tk,WORD)
multi.text.pack()
