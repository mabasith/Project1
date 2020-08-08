from tkinter import *
root = Tk()

v=IntVar()
v.set(1)

lauguages = [('python', 1),('Perl',2),('C++',3),('java',4),('PhP',5)]

def ShowChoice():
    print(v.get())

Label(root, text="""Choose your favorite 
programming language""", justify = LEFT, padx = 20).pack()

for txt,val in lauguages:
    Radiobutton(root,text=txt,indicatoron = 0,width = 20, padx = 20, variable = v,command=ShowChoice,value=val).pack(anchor=W)
mainloop()