
# inheritance 


class Person():
    def __init__(self , first_name ,last_name):
        self.first_name = first_name
        self.last_name = last_name

    def print_details(self):
        print("from Base class", self.first_name)
        print("from Base class",self.last_name)


class clan(Person):
    pass
    

p1 = clan("Bhavit","Mathangi")
p1.print_details()

p1.first_name = "Mohit"
p1.print_details()