#will create rectangle
from tkinter import *

canvas_width = 300
canvas_height = 200

colours = ("#476042", 'yellow')
box = []

for ratio in (0.2, 0.35):
    box.append((canvas_width * ratio, canvas_height * ratio, canvas_width * (1-ratio), canvas_height * (1-ratio)))
master = Tk()

w=Canvas(master, width=200, height= 100)
w.pack()

w.create_rectangle(50, 20, 150, 80, fill="#ff0000")
w.create_rectangle(65, 35, 135, 65, fill="#ff0000")
w.create_line(0,0,50,20,fill="#ff0000",width =3)
w.create_line(0,100,50,80,fill="#ff0000",width =3)
w.create_line(150,20,200,0,fill="#ff0000",width =3)
w.create_line(150,80,200,100,fill="#ff0000",width =3)

#let's modify the top code

w = Canvas(master, width = canvas_width,height=canvas_height)

w.pack()

for i in range(2):
    w.create_rectangle(box[i][0], box[i][1], box[i][2], box[i][3], fill = colours[i])
w.create_line(0,0,box[0][0],box[0][i], fill=colours[0],width =5)
w.create_line(0,canvas_height,box[0][0],box[0][3], fill=colours[0],width =5)
w.create_line(box[0][2],box[0][1],canvas_width,0, fill=colours[0],width =8)
w.create_line(box[0][2],box[0][3],canvas_width,canvas_height, fill=colours[0],width =8)

w.create_text(canvas_width/2, canvas_height/2,text = "Close To Paint")

mainloop()