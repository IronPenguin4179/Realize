#-----------------------------------------------------------------------
# Program name: Realize
# Author: Justin Walker
# Date: 01/16/18
# Purpose: To create a visualization of the relationships between
# classes, their methods, their instances, and their calls.
#-----------------------------------------------------------------------
# GLOBAL VARIABLE DEFINITIONS
#-----------------------------------------------------------------------
# CONSTANT DEFINITIONS
#-----------------------------------------------------------------------
# FUNCTION DEFINITIONS
    # Function Variable Definitions

from text_analysis import Realize

#Opens file lines into an array and removes the white space gaps between lines.
with open('example_files/example.py', 'r') as f:
    FILE = f.readlines()
    file_no_wht = []
    for line in FILE:
        if not line.isspace():
            file_no_wht.append(line)
    FILE_NO_WHT = file_no_wht.copy()

def main():
    realize = Realize(FILE_NO_WHT)
    realize.find_classes()
    realize.scan_imports()
    for classy in realize.classes_dict:
        realize.classes_dict[classy][1].find_methods()
        realize.classes_dict[classy][1].find_class_instances()

#-----------------------------------------------------------------------
# PROGRAM'S MAIN LOGIC
if __name__ == "__main__":
    main()