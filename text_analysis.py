with open('example.py', 'r') as f:
    FILE = f.readlines()
    FILE_NO_WHT = []
    for line in FILE:
        if not line.isspace():
            FILE_NO_WHT.append(line)

class Realize:
    classes_dict = {} #Class_name => [index,obj]
    def __init__(self, file):
        self.data_arr = file

    def add_class(self, class_name, line_number):
        class_obj = Class_obj(class_name, line_number )
        self.classes_dict[class_name] = [line_number, class_obj]

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


class Class_obj(Realize):
    def __init__(self, name, start_line_number):
        self.class_name = name
        self.start_line_number = start_line_number
        self.end_line_number = find_last_line(FILE_NO_WHT, start_line_number)
        self.class_lines = FILE_NO_WHT[self.start_line_number:self.end_line_number]
        self.method_calls = {} #Format { "method_name":[[line_called, instance_name]] }
        self.class_instances = {} #Format { "instance_name":line_created}

    def find_methods(self): 
        for line in self.class_lines:
            pass


#Takes a line and the last line's indent level and outputs line type and it's indent level.
#Used for finding if a line is part of a previous class/function or starting other component.
def check_indent(line, previous_indent_level=0):
        line_type = None
        left_spaces = len(line.rstrip())-len(line.strip())
        indent_level = int(left_spaces/4)

        if indent_level == previous_indent_level:
            line_type = "same"
        elif line.isspace():
            line_type = "blank"
            indent_level = previous_indent_level
        elif indent_level == 0:
            line_type = "zeroed"
        elif indent_level == previous_indent_level+1:
            line_type = "increase"
        elif indent_level == previous_indent_level-1:
            line_type = "decrease"
        else:
            line_type = "other"
            indent_level = previous_indent_level

        return indent_level, line_type

#Used for finding where a class/method ends. Line number is last used line, not whitespace.
def find_last_line(file, start_line_number):
    start_indent_level = check_indent(file[start_line_number-1])#line number is index+1
    line_number = start_line_number
    indent_level = 0
    line_type = None
    while line_type != "zeroed" and line_number <= len(file):
        indent_level, line_type = check_indent(file[line_number-1], indent_level)
        print("Line ",line_number, " is ",line_type, " to ",indent_level)
        line_number += 1
        
    return line_number

def main():
    realize = Realize(FILE_NO_WHT)
    realize.find_classes()
    for classy in realize.classes_dict:
        realize.classes_dict[classy][1].find_methods()
    #print(realize.classes_dict)
    #print(realize.classes_dict["Rectangle"][1].end_line_number)
#######################################
if __name__ == "__main__":
    main()

#print(check_indent(FILE[6],2))