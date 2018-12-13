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


display = tk.Entry(window).grid(columnspan=5, row=0)
tk.Button(window, text='7').grid(column=0, row=1)
tk.Button(window, text='8').grid(column=0, row=1)
tk.Button(window, text='9').grid(column=0, row=1)
tk.Button(window, text='C').grid(column=0, row=1)
tk.Button(window, text='4').grid(column=0, row=1)
tk.Button(window, text='5').grid(column=0, row=1)
tk.Button(window, text='6').grid(column=0, row=1)
tk.Button(window, text='x').grid(column=0, row=1)
tk.Button(window, text='/').grid(column=0, row=1)
tk.Button(window, text='1').grid(column=0, row=1)
tk.Button(window, text='2').grid(column=0, row=1)
tk.Button(window, text='3').grid(column=0, row=1)
tk.Button(window, text='+').grid(column=0, row=1)
tk.Button(window, text='-').grid(column=0, row=1)
tk.Button(window, text='0').grid(column=0, row=1)
tk.Button(window, text='.').grid(column=0, row=1)
tk.Button(window, text='=').grid(column=0, row=1)
