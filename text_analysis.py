with open('example.py', 'r') as f:
    FILE = f.readlines()

class Realize:
    classes_dict = {} #Class_name => [index,obj]

    def __init__(self, file):
        self.data_arr = file
        self.contains = []
        self.instances = {}
        self.methods = {}

    def add_class(self, class_name, index):
        class_obj = Class_obj()
        self.classes_dict[class_name] = [index, class_obj]

    #Takes a line and the last line's indent level and outputs line type and it's indent level.
    #Used for finding if a line is part of a previous class/function or starting other component.
    def __check_indent(self, line, previous_indent_level=0):
        line_type = None
        left_spaces = len(line.rstrip())-len(line.strip())
        indent_level = left_spaces/4

        if indent_level == previous_indent_level:
            line_type = "same"
        elif indent_level == previous_indent_level+1:
            line_type = "increase"
        elif indent_level == previous_indent_level-1:
            line_type = "decrease"
        elif indent_level == 0 and not line.isspace():
            line_type = "blank"
            indent_level = previous_indent_level
        elif indent_level == 0:
            line_type = "zeroed"
        else:
            line_type = "other"
            indent_level = previous_indent_level

        return line_type, indent_level

    #Scans the file to find where the class declarations are, make them a class_object,
    #add it to the classes dictionary and record the index in realize.
    def find_classes(self):
        line_number = 1
        for line in self.data_arr:
            if line.lstrip()[0:6] == "class ":
                print(line_number, line)
                class_name = line.strip()[6:-1]
                self.add_class(class_name, line_number)
            line_number += 1

    def find_methods(self):
        pass
        
class Class_obj(Realize):
    def __init__(self):
        self.methods = []

    def find_methods(self):
        keys = self.classes_dict.keys()

def main():
    realize = Realize(FILE)
    realize.find_classes()
    for classy in realize.classes_dict:
        realize.classes_dict[classy][1].find_methods()
    print(realize.classes_dict)

#######################################
if __name__ == "__main__":
    main()