class Rectangle:
    def __init__(self):
        self.x1 = def_x1
        self.y1 = def_y1
        self.x2 = def_x2
        self.y2 = def_y2
    
    def create(self):
        canvas.create_rectangle(self.x1,self.y1,self.x2,self.y2)
        self.x1 = self.x1+def_x2+def_gap
        self.x2 = self.x1+(def_x2-def_x1)
        print(self.x1, self.x2)

rect = Rectangle()
rect.create()
rect.create()
rect.create()