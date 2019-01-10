with open('example.py', 'r') as f:
    lines = f.readlines()

#Takes a line and the last line's indent level and outputs line type and it's indent level.
#Used for finding if a line is part of a previous class/function or starting other component.
def analyze(line, previous_indent_level=0):
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
    
current_level = 0
for line in lines:
  type, current_level = analyze(line,current_level)
  print(type,current_level)