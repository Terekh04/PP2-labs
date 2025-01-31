class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        print(f"Point({self.x}, {self.y})")
    
    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
    
    def dist(self, other_point):
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5
    
x1 = int(input("Write x1: "))
y1 = int(input("Write y1: "))
p1 = Point(x1, y1)
x2 = int(input("Write another x2: "))
y2 = int(input("Write another y2: "))
p2 = Point(x2, y2)
p1.show()  
p2.show()  
newx1 = int(input("Write new x1: "))
newy1 = int(input("Write new y1: "))
p1.move(newx1, newy1)
p1.show()
print("Distance between points:", p1.dist(p2)) 