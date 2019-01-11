with open('example.py', 'r') as f:
    lines = f.readlines()

class Realize:
    c_index = [] #Contains [index, class_obj]
    classes = {} 
    
    def __init__(self):
        self.contains = []
        self.instances = {}
        self.methods = {}

    def add_class(self, class_name, index):
        class_obj = Realize
        self.c_index.append([index, class_obj])
        self.classes[class_name] = class_obj

#Takes a line and the last line's indent level and outputs line type and it's indent level.
#Used for finding if a line is part of a previous class/function or starting other component.
def check_indent(line, previous_indent_level=0):
    line_type = None
    left_spaces = len(line.rstrip())-len(line.strip())
    indent_level = left_spaces/4

    if indent_level == previous_indent_level:
        line_type = "same"
    elif indent_level == previous_indent_level+1:
        line_type = "increase"
    elif indent_level == previous_indent_level-1:
        line_type = "decrease"
    elif indent_level == 0 and len(line.strip()) == 0:
        line_type = "blank"
        indent_level = previous_indent_level
    elif indent_level == 0:
        line_type = "zeroed"
    else:
        line_type = "other"
        indent_level = previous_indent_level

    return line_type, indent_level

#Scans the file to find where the class declarations are, make them a class_object, add it to the classes dictionary and record the index in realize.
def find_classes(lines, classy):
    line_number = 1
    for line in lines:
        if line.lstrip()[0:6] == "class ":
            print(line_number, line)
            class_name = line.strip()[6:]
            classy.add_class(class_name, line_number)

        line_number += 1    

def main():
    realize = Realize()
    find_classes(lines, realize)
    print(realize.classes)


#######################################
if __name__ == "__main__":
    main()