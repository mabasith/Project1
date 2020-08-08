from tkinter import *

canvas_width = 400
canvas_height = 400
python_green = "#476042"

def polygon_star(canvas, x, y, p, t, outline=python_green, fill ='yellow', width = 1):
    points = []
    for i in (1, -1):
        points.extend((x, y+i*p))
        points.extend((x+i*t, y+i*t))
        points.extend((x + i*p, y))
        points.extend((x+i*t, y-i*t))

    print(points)

    canvas.create_polygon(points, outline=outline,fill=fill,width=width)
master = Tk()

w = Canvas(master, width=canvas_width,height=canvas_height)
w.pack()

p = 50
t = 15

nsteps = 10
step_x = int(canvas_width/nsteps)
step_y = int(canvas_height/nsteps)

for i in range(1,nsteps):
    polygon_star(w,i*step_x,i*step_y,p,t,outline='red',fill='green',width=3)
    polygon_star(w,i*step_x,canvas_height-i*step_y,p,t, outline='red',fill='green',width=3)
mainloop()

#oval object widgets

def checkered(canvas, line_distance):
    for x in range(line_distance, canvas_width, line_distance):
        canvas.create_line(x,0,x,canvas_height,fill='#476042')
    for y in range(line_distance, canvas_width, line_distance):
        canvas.create_line(0,y,canvas_width,y,fill='#476042')
master = Tk()
canvas_width = 200
canvas_height = 200

w=Canvas(master,width = canvas_width,height=canvas_height)
w.pack()
checkered(w,10)
mainloop()

canvas_width = 300
canvas_height = 80

master = Tk()
canvas = Canvas(master, width=canvas_width, height= canvas_height)
canvas.pack()
bitmaps = ['error','gray75','gray50','gray25','gray12','hourglass','info','questhead']
nsteps = len(bitmaps)
step_x = int(canvas_width/nsteps)

for i in range(0, nsteps):
    canvas.create_bitmap((i+1)*step_x - step_x/2, 50, bitmap=bitmaps[i])
mainloop()