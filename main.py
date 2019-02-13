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

from tkinter_draw import *

def main():
    gui = Gui_class(root)
    root.mainloop()

#-----------------------------------------------------------------------
# PROGRAM'S MAIN LOGIC
if __name__ == "__main__":
    main()