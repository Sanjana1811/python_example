

# compile time polymorphism 
#  what this does  is  it compiles the code and then  checks which function to executed 

# class Calculator():
#     def  calculate(self ,a ,b):
#         return a+b
    
#     def calculate(self , a ,b, c):
#         return a+b+c
    

# c1 = Calculator()
# c1.calculate(1,2)


class Calculator():

    def  calc(self ,a ,b):
        return a+b
    
    def calc(self, *args):
        return sum(args)
    

c2 = Calculator()
sum_of = c2.calc()
print("Summation" ,sum_of)