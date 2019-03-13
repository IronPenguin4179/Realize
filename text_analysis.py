class Realize:
    def __init__(self, file_name):
        new_file_name = remove_path(file_name)
        with open(file_name,'r') as f:
            self.data_arr = self.remove_file_whitelines(f)
        self.base_file_name = new_file_name
        self.imported_files_dict = {} #{"file_name":"what to import"}
        self.file_classes_dict = {}
        self.classes_dict = {} #{"name":[line_number,class_obj]}

    def find_import_statements(self):
        data = self.data_arr
        imports = []
        for line in data:
            liner = line.lstrip()
            if liner[0:7] == "import ":
                imports.append(line.strip())
            elif liner[0:5] == "from ":
                imports.append(line.strip())
        return imports

    def find_import_names(self):
        #Scans through import statements to find what classes to import and files
        #to import from.
        #Adds information to self.imported_files_dict {"file_name":["class_name"]}
        list_of_imports = self.find_import_statements()
        for item in list_of_imports:
            index_of_from = item.find("from ")
            index_of_import = item.find("import ")
            item_length = len(item)
            from_length = len("from ")
            import_length = len("import ")

            if index_of_from == 0:
                name_of_class = item[index_of_import+import_length:item_length+1]
            
                file_index = index_of_from + from_length
                file_name = item[file_index:index_of_import]
            else:
                name_of_class = "*"
                file_name = item[import_length:item_length+1]

            if file_name in self.imported_files_dict:
                self.imported_files_dict[file_name].append(name_of_class)
            else:
                self.imported_files_dict[file_name] = [name_of_class]

        iter_hash = iter(self.classes_dict)
        keys = []
        for i in range(0,len(self.classes_dict)):
            keys.append(next(iter_hash))

        self.imported_files_dict[self.base_file_name] = keys
        print(self.imported_files_dict)


    def get_dict(self):
        return self.classes_dict

    def add_class(self, class_name, line_number, file_name):
        class_obj = Class_obj(class_name, line_number, self.data_arr)
        self.classes_dict[class_name] = [line_number, class_obj, file_name]

    def remove_file_whitelines(self, file):
        f = file.readlines()
        file_no_wht = []
        for line in f:
            if not line.isspace():
                file_no_wht.append(line)
        return file_no_wht

    #Scans the file to find where the class declarations are, make them a class_object,
    #add it to the classes dictionary and record the index in realize.
    def find_classes(self,file_name):
        with open(file_name,'r') as f:
            file_arr = self.remove_file_whitelines(f)
        new_name = remove_path(file_name)
        line_number = 1
        for line in file_arr:
            if line.lstrip()[0:6] == "class ":
                class_name = line.strip()[6:-1]
                self.add_class(class_name, line_number, new_name)
            line_number += 1

    def clean_up_imports(self):
        for file in self.imported_files_dict:
            for classy in self.imported_files_dict[file]:
                classy = classy.capitalize()
                comma = classy.find(',')
                asterisk = classy.find('*')
                if comma != -1:
                    while comma != -1:
                        self.imported_files_dict[file].append(classy[0:comma])
                        classy = classy[comma+1:].capitalize().strip()
                        comma = classy.find(',')
                    self.imported_files_dict[file][0] = classy.capitalize()
                elif asterisk != -1:
                    arr = []
                    for classes in self.classes_dict:
                        for attr in self.classes_dict[classes]:
                            if attr == file:
                                arr.append(classes.capitalize())
                            self.imported_files_dict[file] = arr
        print(self.imported_files_dict)

class Class_obj:
    def __init__(self, name, start_line_number, file):
        self.class_name = name
        self.data = file.copy()
        self.start_line_number = start_line_number
        self.end_line_number = self.find_last_line(self.data, start_line_number)
        self.class_lines = self.data[self.start_line_number:self.end_line_number]
        self.method_calls = {} #Format { "method_name":[[line_called, instance_name]] }
        self.class_instances = {} #Format { "instance_name":line_created}

    #Unfinished
    def find_methods(self): 
        index = self.start_line_number
        for line in self.class_lines:
            if line.strip()[0:4] == "def ":
                parentheses = line.strip().index("(")
                self.method_calls[line.strip()[4:parentheses]] = []

    #Unfinished
    def find_class_instances(self):
        line_number = 1
        data = self.data
        for line in data:
            if line.find(self.class_name) != -1 and line.lstrip()[0:6] != "class ":
                print("Instance found at",line_number)
            line_number += 1


    #Takes a line and the last line's indent level and outputs line type and it's indent level.
    #Used for finding if a line is part of a previous class/function or starting other component.
    @staticmethod
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

    #Iterates through lines in file to find where class ends. 
    #Takes array of lines from file and the line number where the class begins.
    #Returns the number of the last line in the class
    def find_last_line(self, file, start_line_number):
        line_number = start_line_number-1
        start_indent_level = self.check_indent(file[line_number])#line number is index+1
        indent_level = 0
        line_type = None
        while line_type != "zeroed" and line_number <= len(file):
            line_number += 1
            indent_level, line_type = self.check_indent(file[line_number-1], indent_level)
        else:
            line_number -= 1
        return line_number

def remove_path(name):
    name+=" "
    slash = name.find('/')+1
    checker = 0
    while slash != checker:
        checker = slash
        slicer = name[slash:-1]
        slash += slicer.find('/')+1
    dot = slicer.find('.')
    file_name = slicer[0:dot]
    return file_name

""" realizey = Realize('example_files/example.py')
realizey.find_classes('example_files/example.py')
realizey.find_import_names()
for classy in realizey.classes_dict:
    realizey.classes_dict[classy][1].find_methods()
    realizey.classes_dict[classy][1].find_class_instances()
for filey in realizey.imported_files_dict:
    realizey.find_classes('example_files/'+filey.rstrip()+'.py')
realizey.clean_up_imports() """
