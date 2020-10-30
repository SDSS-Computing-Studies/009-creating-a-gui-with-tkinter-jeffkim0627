import tkinter as tk 
from tkinter import *
from tkinter import ttk


window = tk.Tk()
window.title("tk")

window.geometry("400x50")



lable1 = tk.Label(window, text="x", borderwidth=2, relief=SUNKEN)
button1 = tk.Button(window,text="=")

entry1 = tk.Entry(window,text="Entry widgets can be typed in", width=14, borderwidth=2, relief=SUNKEN)
entry2 = tk.Entry(window,text="Entry widgets can be typed in", width=14, borderwidth=2, relief=SUNKEN)
entry3 = tk.Entry(window,text="Entry widgets can be typed in", width=28, borderwidth=2, relief=SUNKEN)





lable1.grid(row = 1, column = 2)
button1.grid(row = 1, column = 4)

entry1.grid(row = 1, column = 1)
entry2.grid(row = 1, column = 3)
entry3.grid(row = 1, column = 5)


window.mainloop()