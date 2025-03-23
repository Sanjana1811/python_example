# class Area():
#     def __init__(self, length, width, height):
#         self.length = length
#         self.width = width
#         self.height = height

#     def square(self):
#         print('area of square : ', self.width * self.width)

#     def rectangle(self):
#         print('area of rectangle : ', self.length * self.width)

#     def cube(self):
#         print('area of a cube :', (self.length * self.length * self.length))
       
# sqr_area = Area(4,4,8)
# sqr_area.square()
# sqr_area.rectangle()
# sqr_area.cube()




class rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width 
        print("Area of rectangle = ", self.length * self.width )

rectangle1 = rectangle(5, 5)
# print(rectangle1)