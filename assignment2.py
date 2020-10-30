import tkinter as tk 
from tkinter import *
from tkinter import ttk


window = tk.Tk()
window.title("T-Town Veterinary Clinic Database")

window.geometry("400x200")

dogphoto = PhotoImage(file="dog.png")
label1 = tk.Label(window, image=dogphoto)
label2 = tk.Label(window, text="                     ")
label3 = tk.Label(window, text="Client Database")
label4 = tk.Label(window, text="Name")
label5 = tk.Label(window, text="Type")
label6 = tk.Label(window, text="Breed")
label7 = tk.Label(window, text="Owner")
label8 = tk.Label(window, text="Birthdate")
Button1 = tk.Button(window,text="Search by Name")
entry1 = tk.Entry(window,text="", width=10, borderwidth=2, relief=SUNKEN)
entry2 = tk.Entry(window,text="", width=10, borderwidth=2, relief=SUNKEN)
entry3 = tk.Entry(window,text="", width=10, borderwidth=2, relief=SUNKEN)
entry4 = tk.Entry(window,text="", width=10, borderwidth=2, relief=SUNKEN)
entry5 = tk.Entry(window,text="", width=10, borderwidth=2, relief=SUNKEN)
entry6 = tk.Entry(window,text="", width=10, borderwidth=2, relief=SUNKEN)





label1.grid(row = 1, column = 1)
label2.grid(row = 1, column = 2)
label3.grid(row = 1, column = 3)
label4.grid(row = 2, column = 1)
label5.grid(row = 2, column = 2)
label6.grid(row = 2, column = 3)
label7.grid(row = 2, column = 4)
label8.grid(row = 2, column = 5)

Button1.grid(row = 1, column = 4)
entry1.grid(row = 1, column = 5)
entry2.grid(row = 3, column = 1)
entry3.grid(row = 3, column = 2)
entry4.grid(row = 3, column = 3)
entry5.grid(row = 3, column = 4)
entry6.grid(row = 3, column = 5)


window.mainloop()