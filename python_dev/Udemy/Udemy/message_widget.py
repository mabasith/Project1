from tkinter import *
from tkinter import ttk
master = Tk()
whatever_you_do = "Welcome to Advanced Python programming course. I love Python!"
msg = Message(master, text = whatever_you_do)

msg.config(bg="red", font=('times', 22, "italic"))
msg.pack()
mainloop()

# we will create image box with python image

canvas_width = 600
canvas_height = 600

master = Tk()

canvas = Canvas(master, width = canvas_width, height=canvas_height)
canvas.pack()
img = PhotoImage(file = "/home/hitech/Documents/python_dev/Udemy/tree.png")
canvas.create_image(20,20,anchor = NW, image=img)
mainloop()

lastx, lasty = 0,0
def xy(event):
    global lastx, lasty
    lastx, lasty = event.x, event.y
def addLine(event):
    global lastx, lasty
    canvas.create_line((lastx,lasty,event.x,event.y))
    lastx, lasty = event.x, event.y
root = Tk()
root.columnconfigure(0,weight=1)
root.rowconfigure(0, weight =1)
canvas = Canvas(root)
canvas.grid(column=0, row=0, sticky=(N,W,E,S))
canvas.bind("<Button-1>", xy)
canvas.bind("<B1-Motion>", addLine)

root.mainloop()
