from tkinter import *

root = Tk()

class Gui_class():
    def __init__(self, master,obj):
        self.master = master
        self.obj = obj.copy()
        self.leftFrame = Frame(master, width=540, height=400, background="bisque")
        self.rightFrame = Frame(master, width=100, height=350, background="#b22222")
        self.leftFrame.grid(column=0,row=0)
        self.rightFrame.grid(column=1,row=0)

        self.master.grid_rowconfigure(1, weight=1)
        self.master.grid_columnconfigure(0, weight=1)

        self.label2 = Frame(self.rightFrame, width=100,height=100,bg="green")
        self.label2.grid(row=0,sticky="n")
        self.button = Button(self.rightFrame,text="Classes",command=self.showClasses)
        self.button.grid(row=1)

    def showClasses(self):
        print(self.obj)