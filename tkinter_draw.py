from os import path
from tkinter import *
from tkinter import filedialog
from text_analysis import Realize

root = Tk()
root.geometry("400x300")
root.configure(background="grey")
root.title("Realize")
root.grid_columnconfigure(0, weight=3)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(0,weight=1)
#root.grid_columnconfigure(2, weight=1)
#root.grid_columnconfigure(3, weight=2)

class Gui_class():
    def __init__(self, master):
        self.master = master
        #self.classes = classes.copy()

    def main_frames(self):
        self.left_frame = Frame(self.master)
        self.right_frame = Frame(self.master,height=200,bg="black")

        self.left_frame.grid(column=0,row=0,sticky="nsew")
        self.right_frame.grid(column=1,row=0,sticky="nsew")

    def header(self):
        #Menu header
        self.menu_bar = Menu(self.master)
        self.master.config(menu=self.menu_bar)
        
        #File menu
        self.file_menu = Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Open", command=self.filePicker)
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
        frame = self.right_frame
        #Side panel
        #self.master.config(menu=self.menu_bar)
        #self.side_panel = Frame(self.master,height=200,bg="black")
        #self.side_panel.grid(column=4,row=1,rowspan=10,sticky="nsew")

        #Show classes button
        #self.show_classes_button = Button(self.master,text="Classes",command=self.showClasses)
        #self.show_classes_button.grid(column=4,row=1,sticky="ew")

        #Entry bar and find button
        self.entry = Entry(frame)
        #self.entry.grid(column=4,row=2,sticky="ew")
        self.entry.pack()
        self.find_it_button = Button(frame,text="Find it!",command=self.displayClassInfo)
        #self.find_it_button.grid(column=4,row=3,sticky="ew")
        self.find_it_button.pack()

    def showClasses(self):
        i = 1
        for classy in self.classes:
            self.class_label = Label(self.left_frame,text=classy)
            self.class_label.grid(column=0,row=i,sticky="nsew",pady=3)
            i+=1

    def hello(self):
        print("Hello")

    def filePicker(self):
        file_pick = filedialog.askopenfilename(initialdir= path.dirname(__file__))
        
        with open(file_pick, 'r') as f:
            FILE = f.readlines()
            file_no_wht = []
            for line in FILE:
                if not line.isspace():
                    file_no_wht.append(line)
            FILE_NO_WHT = file_no_wht.copy()
        self.file = FILE_NO_WHT
        self.realize_file()

    def realize_file(self):
        self.realize = Realize(self.file)
        self.realize.find_imports()
        self.realize.scan_imports()
        self.realize.find_classes()
        for classy in self.realize.classes_dict:
            self.realize.classes_dict[classy][1].find_methods()
            self.realize.classes_dict[classy][1].find_class_instances()
        #print(self.realize.classes_dict)

    def displayClassInfo(self):
        frame = self.left_frame
        self.class_label = Label(frame, text=self.entry.get())
        exists = False
        for item in self.classes:
            if item == self.entry.get():
                exists = True
        if exists:
            self.class_label = Label(frame, text=self.entry.get())
        else:
            self.class_label = Label(frame, text="Entry not found.")
        #self.class_label.grid(column=0,row=1,sticky="nwes")
        self.class_label.pack()


    def run(self):
        self.main_frames()
        self.header()
        self.sidebar()

new = Gui_class(root)
new.run()
root.mainloop()