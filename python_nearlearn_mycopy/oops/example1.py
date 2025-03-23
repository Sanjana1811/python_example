
class Area:
    def __init__(self, length, width=0, height=0):
        self.length = length
        self.width = width
        self.height = height


class Square(Area):
    def __init__(self, length):
        super().__init__(length)

    def area(self):
        return self.length ** 2

class Rectangle(Area):
    def __init__(self, length, width):
        super().__init__(length, width)

    def area(self):
        return self.length * self.width


class Cube(Area):
    def __init__(self, length):
        super().__init__(length)

    def area(self):
        return (self.length*self.length*self.length)


sqr = Square(5)
rec = Rectangle(5, 10)
cube = Cube(4)

print("Area of Square:", sqr.area())
print("Area of Rectangle:", rec.area())
print("Surface Area of Cube:", cube.area())


# # length, width, height 

# class Area():
#     def __init__(self, length, width, height):
#         self.length = length
#         self.width = width
#         self.height = height

#     def square(self):
#         print('area of square : ', self.length * self.width)

#     def rectangle(self):
#         print('area of rectangle : ', self.length * self.width)

#     def cube(self):
#         print('area of a cube :', (6 * (self.length**2)))


# class Square(Area):
#     def __init__(self, length, width,height):
#        super().__init__(length,width,height)     

#     def area(self):
#         return self.length ** 2
    
# class Rectangle(Area):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width  
    
# # class Cube(Area):
# #       def __init__(self, length, width,height):
# #         super().__init__(length, width,height)

# #       def area(self):
# #         # Surface area of a cube: 6 * (side_length^2)
# #         return 6 * super().area()
# sqr_area = Area(5,5,7)
# sqr = Square(5,5,7)
# rec = Rectangle(5,5,7)
# # cube_area = Cube(5,5,7)

# sqr.area()
# rec.area()
# cube_area.area()

# # sqr_area.square()
# # sqr_area.rectangle()
# # sqr_area.cube()