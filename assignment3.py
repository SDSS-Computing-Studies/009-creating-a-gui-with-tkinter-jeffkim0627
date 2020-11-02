import tkinter as tk 
from tkinter import *
from tkinter import ttk


window = tk.Tk()
window.title("Example")

window.geometry("300x140")

dogphoto = PhotoImage(file="dog.png")
label0 = tk.Label(window, text="                       ")
label1 = tk.Label(window, image=dogphoto)
label2 = tk.Label(window, text="Pochacco!")
label3 = tk.Label(window, text="                       ")

label4 = tk.Label(window, text="    A cuddly little puppy! This is from the same \n creators who brought you Keropi and Kero Kero", background="#BEE0E5")




label0.grid(row=1, column=1)
label1.grid(row=1, column=2)
label2.grid(row=1, column=3)
label3.grid(row=1, column=4)
label4.grid(row=2, column=1, rowspan=2, columnspan=4)


window.mainloop()