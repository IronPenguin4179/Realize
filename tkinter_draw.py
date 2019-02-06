from tkinter import *

root = Tk()
root.configure(background="grey")
root.title("Realize")

class Gui_class():
    def __init__(self, master, classes):
        self.master = master
        self.classes = classes.copy()

    def header(self):
        #Menu header
        self.header = Label(bg="red", width=100)
        self.header.grid(columnspan=5, row=0, column=0)
        self.menu_bar = Menu(root)

        #File menu
        self.file_menu = Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Open", command=self.hello)
        self.file_menu.add_command(label="Save", command=self.hello)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=root.quit)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        #Edit menu
        self.edit_menu = Menu(self.menu_bar, tearoff=0)
        self.edit_menu.add_command(label="Cut", command=self.hello)
        self.edit_menu.add_command(label="Copy", command=self.hello)
        self.edit_menu.add_command(label="Paste", command=self.hello)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)

        #Help menu
        self.help_menu = Menu(self.menu_bar, tearoff=0)
        self.help_menu.add_command(label="About", command=self.hello)
        self.menu_bar.add_cascade(label="Help", menu=self.help_menu)

    def sidebar(self):
        #Side panel
        self.master.config(menu=self.menu_bar)
        self.side_panel = Frame(self.master,height=200,bg="black")
        self.side_panel.grid(column=4,row=1,rowspan=10,sticky="nsew")

        #Show classes button
        #self.show_classes_button = Button(self.master,text="Classes",command=self.showClasses)
        #self.show_classes_button.grid(column=4,row=1,sticky="ew")

        #Entry bar and find button
        self.entry = Entry(self.master)
        self.entry.grid(column=4,row=2,sticky="ew")
        self.find_it_button = Button(self.master,text="Find it!",command=self.displayClassInfo)
        self.find_it_button.grid(column=4,row=3,sticky="ew")

    def showClasses(self):
        i = 1
        for classy in self.classes:
            self.class_label = Label(self.master,text=classy)
            self.class_label.grid(column=0,row=i,sticky="nsew",pady=3)
            i+=1

    def hello(self):
        print("Hello")

    def displayClassInfo(self):
        self.class_label = Label(self.master, text=self.entry.get())
        exists = False
        for item in self.classes:
            if item == self.entry.get():
                exists = True
        if exists:
            self.class_label.grid(column=0,row=1,sticky="nwes")

    def run(self):
        self.header()
        self.sidebar()

new = Gui_class(root,["thing","foo","barthalomew"])
new.run()
root.mainloop()