

# creating a stack using class 

class Stack():
    def __init__(self):
        self.values = []
    
    # appening to  the stack
    def push(self,val):
        self.values.append(val)

    # finding the length of the stack 
    def lenght(self):
        if len(self.values == 0):
            print("List is empty")
        else:
            print("List is not empty")
    
    # peek the  last element
    def peek(self):
        print(self.values[-1])

    # pop  the element from the stack 
    def remove(self,val):
        if val in self.values:
            print("ELement popped",self.values.pop(val))
        else:
            print("No Element in the stack")

    # gettint the size of the stack
    def size(self):
        print("Size of the stack is",len(self.values))
     
    