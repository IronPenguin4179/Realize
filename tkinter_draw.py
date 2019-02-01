from tkinter import *

root = Tk()
root.configure(background="black")

class Gui_class():
    def __init__(self, master, classes):
        self.master = master
        self.classes = classes.copy()

        self.header = Label(bg="red", width=100)
        self.header.grid(columnspan=5, row=0, column=0)

        #self.file_menu = Menu(master, text="File")
        #self.file_menu.grid(row=0,column=0)

        self.side_panel = Frame(master,height=200,bg="green")
        self.side_panel.grid(column=4,row=1,rowspan=10,sticky="nsew")
        self.button = Button(master,text="Classes",command=self.showClasses)
        self.button.grid(column=4,row=1,sticky="ew")

    def showClasses(self):
        i = 1
        for classy in self.classes:
            self.class_label = Label(self.master,text=classy)
            self.class_label.grid(column=0,row=i,sticky="nsew",pady=3)
            i+=1