from os import path
from tkinter import filedialog

file = filedialog.askopenfilename(initialdir= path.dirname(__file__))
print(file)