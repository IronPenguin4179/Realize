text1 = "class Rectangle(a,s,d,f):"
text2 = "    def __init__(self):"
text3 = "        self.thing = true"

if text1[0:5] == "class":
    n = len("class ")
    space = True
    while(space==True):
        if text1[n] != " ":
          space = False
        else:
          n+=1