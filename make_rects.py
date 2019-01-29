from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("700x500")
canvas = Canvas(root)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
canvas.grid(column=0, row=0, sticky=(N, W, E, S))

def_x1 = 10
def_y1 = 10
def_x2 = 150
def_y2 = 80
def_gap = 20
def add_col():
    x_1 = x1+x2+gap
    x_2 = x1+x2
    print(x1, x2)

    return x_1, y1, x_2, y2
    
class Rectangle:
    def __init__(self):
        self.rects = [] #format[[x1,y1,x2,y2]]
    
    def create(self, x1, y1, x2, y2):
        canvas.create_rectangle(x1,y1,x2,y2)
        self.x1 = self.x1+def_x2+def_gap
        self.x2 = self.x1+(def_x2-def_x1)
        print(self.x1, self.x2)

rect = Rectangle()
rect.create()
rect.create()
rect.create()
root.mainloop()