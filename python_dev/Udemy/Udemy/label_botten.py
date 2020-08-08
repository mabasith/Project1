import tkinter
from tkinter import ttk

root = tkinter.Tk()
style = ttk.Style()
style.map("C.TButton", foreground =[('pressed','red'), ('active', 'blue')],background=[('pressed','!disabled','black'),('active','white')])
colored_btn = ttk.Button(text="Click Me!", style = "C.TButton").pack()
root.mainloop()