

class Shape():
    def area(self):
        pass

class Square(Shape):
    def __init__(self,side):
        self.side = side
    
    def area(self):
        return f"Area of square {self.side * self.side}"
    
class Circle(Shape):
    def __init__(self ,radius):
        self.radius = radius

    def area(self):
        return f" Area of Circle is {3.14 * self.radius * self.radius}"


# Run time polymorphism
# This  is Dynamic menas the function area is  there in multiple class but which  area function to called is
# is determined on the run time bsed on the  object were are calling 

shapes = [Square(8),Circle(9)]

for shape in shapes:
    print(shape.area())

