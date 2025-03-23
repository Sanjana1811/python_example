

class Person():

    # constructor 
    def __init__(self , name ,age ,company):
        self.name = name
        self.age = age
        self.company = company
        

    # function 
    def get_details(self):
        print("Name of person" , self.name)
        print("Age of person",self.age)
        print("Company",self.company)
        

    # get_salary of employee

    def get_salary(self):
        if self.age > 20  and self.age < 24:
            print("Salary is 30000")
            print("-------------- \n")
        if self.age > 25 and self.age < 29:
            print("Salary is 70000")
            print("-------------- \n")
        if self.age >=30 and self.age < 54:
            print("Salary is  120000")
            print("-------------- \n")
        

p1 = Person("Tilak" ,50 ,"GCC")   
p1.get_details()
p1.get_salary()


p2 = Person("Bhavit", 26 ,"Skytex")
p2.get_details()
p2.get_salary()

p3 = Person("Vismita", 22 ,"Nearlearn")
p3.get_details()
p3.get_salary()


    
