from tkinter import *

canvas_height = 50
canvas_width = 100

class App:
    def __init__(self, master, width = canvas_width, height=canvas_height):
        frame = Frame( master, width = canvas_width, height = canvas_height)
        frame.pack()
        self.button = Button(frame, text = 'Close', fg='red', command = frame.quit)
        self.button.pack(side = LEFT)
        self.slogan = Button(frame, text ="Click Me!", fg = "blue", command=self.write_slogan)
        self.slogan.pack(side=LEFT)
        self.button.config(height= 2, width= 20)
        self.slogan.config(height=2, width=20)
    def write_slogan(self):
        print("Welcome to Python Advanced Programming")
root = Tk()
root.title("Hello World")
app = App(root)
root.mainloop()

#This code is for the timer

import tkinter as tk
counter = 0

def counter_label(label):
    counter = 0
    def count():
        global counter
        counter +=1
        label.config(text = str(counter))
        label.after(1000,count)
    count()
root = tk.Tk()
root.title("ounting Second")
label = tk.Label(root, fg="dark green")
label.pack()
counter_label(label)
button = tk.Button(root, text = 'Stop', width=55, command = root.destroy)
button.pack()
root.mainloop()