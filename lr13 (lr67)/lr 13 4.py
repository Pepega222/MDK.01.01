from tkinter import *
from tkinter import ttk

root = Tk()
root.title("METANIT.COM")
root.geometry("250x200")

btn = ttk.Button()
btn.pack()
btn.config(text = "Send email")
root.mainloop()