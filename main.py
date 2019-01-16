from text_analysis import Realize

with open('example.py', 'r') as f:
    FILE = f.readlines()
    FILE_NO_WHT = []
    for line in FILE:
        if not line.isspace():
            FILE_NO_WHT.append(line)

def main():
    realize = Realize(FILE_NO_WHT)
    realize.find_classes()
    for classy in realize.classes_dict:
        realize.classes_dict[classy][1].find_methods()
        realize.classes_dict[classy][1].find_class_instances()
#######################################
if __name__ == "__main__":
    main()