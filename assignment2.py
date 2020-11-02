import tkinter as tk 
from tkinter import *
from tkinter import ttk


window = tk.Tk()
window.title("T-Town Veterinary Clinic Database")

window.geometry("400x200")

dogphoto = PhotoImage(file="dog.png")
label1 = tk.Label(window, image=dogphoto)
label3 = tk.Label(window, text="Client Database")
label4 = tk.Label(window, text="Name")
label5 = tk.Label(window, text="Type")
label6 = tk.Label(window, text="Breed")
label7 = tk.Label(window, text="Owner")
label8 = tk.Label(window, text="Birthdate")

Button1 = tk.Button(window,text="Search by Name")
Button2 = tk.Button(window,text="Previous")
Button3 = tk.Button(window,text="Save Entry")
Button4 = tk.Button(window,text="Next")

entry1 = tk.Entry(window,text="", width=10, borderwidth=2, relief=SUNKEN)
entry2 = tk.Entry(window,text="", width=10, borderwidth=2, relief=SUNKEN)
entry3 = tk.Entry(window,text="", width=10, borderwidth=2, relief=SUNKEN)
entry4 = tk.Entry(window,text="", width=10, borderwidth=2, relief=SUNKEN)
entry5 = tk.Entry(window,text="", width=10, borderwidth=2, relief=SUNKEN)
entry6 = tk.Entry(window,text="", width=10, borderwidth=2, relief=SUNKEN)





label1.place(x=0,y=0)
label3.place(x=150, y=50)
label4.place(x=0, y=100)
label5.place(x=85, y=100)
label6.place(x=170, y=100)
label7.place(x=255, y=100)
label8.place(x=340, y=100)

Button1.place(x=230, y=0)
Button2.place(x=0, y=150)
Button3.place(x=180, y=150)
Button4.place(x=360, y=150)

entry1.place(x=330, y=0)
entry2.place(x=0, y=120)
entry3.place(x=85, y=120)
entry4.place(x=170, y=120)
entry5.place(x=255, y=120)
entry6.place(x=340, y=120)


window.mainloop()