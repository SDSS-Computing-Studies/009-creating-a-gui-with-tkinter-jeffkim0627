import tkinter as tk 
from tkinter import *
from tkinter import ttk


window = tk.Tk()
window.title("Example")

window.geometry("260x140")

dogphoto = PhotoImage(file="dog.png")

label1 = tk.Label(window, image=dogphoto)
label2 = tk.Label(window, text="Pochacco!")


label4 = tk.Label(window, text="    A cuddly little puppy! This is from the same \n creators who brought you Keropi and Kero Kero", background="#BEE0E5")





label1.place(x=70, y=0)
label2.place(x=140, y=40)

label4.place(x=0, y=100)


window.mainloop()