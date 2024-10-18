class Point:
    def __init__(self,x,y):  #this is called a constructor (__init__)
        self.x = x
        self.y = y
    def move(self):
        print("move")

    def draw(self):
        print("draw")


point = Point(10,5)
print(point.x)
