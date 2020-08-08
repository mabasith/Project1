from turtle import *

size = 800
min = 64
pf = 0.86660254

def s(l,x,y):
    if l>min:
        l = l/2
        s(l,x,y)#bottom left triangle
        s(l,x+l,y)#bottom right triangle
        s(l,x+l/2,y+l*pf)#top triangle
    else:
        goto(x,y); pendown() #start at(x,y)
        begin_fill()
        forward(l); left(120)
        forward(l); left(120)
        forward(l)
        end_fill()
        setheading(0)#face east
        penup(); goto(x,y)
penup()
speed('fastest')
s(size,-size/2, -size*pf/2.0)
done()

