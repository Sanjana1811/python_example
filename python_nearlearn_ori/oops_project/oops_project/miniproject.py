## lets start with creating the mini project 

class Person:
    '''
    Base class for person 
    containing name, contact, place_from
    '''
    def __init__(self, name, contact, place_from):
        self.name = name
        self.contact = contact
        self.place_from = place_from

    def __str__(self):
        return f"Name: {self.name} \nContact: {self.contact} \nPlace from: {self.place_from}"


class Guest(Person):
    '''
    Inherited class from Base class Person 
    Taking input name, contact, place_from, room_number
    '''
    def __init__(self, name, contact, place_from, room_number):
        super().__init__(name, contact, place_from)
        self.room_number = room_number  

    def __str__(self):
        return f"Guest: {super().__str__()} \nRoom No: {self.room_number}"


class Staff(Person):
    '''
    Inherited from Base class Person
    Taking input name, contact, place_from, employee_id, role
    '''
    def __init__(self, name, contact, place_from, employee_id, role):
        super().__init__(name, contact, place_from)
        self.employee_id = employee_id
        self.role = role

    def __str__(self):
        return f"Staff: {super().__str__()} \nEmployee ID: {self.employee_id} \nRole: {self.role}"


class Room:
    '''
    Room Class taking input room_number, room_type, balcony, ac, room_service, price
    '''
    def __init__(self, room_number, room_type, balcony, ac, room_service, price):
        self.room_number = room_number
        self.room_type = room_type
        self.balcony = balcony
        self.ac = ac
        self.room_service = room_service
        self.price = price
        self.occupied = False

    def __str__(self):
        status = "Occupied" if self.occupied else "Available"
        return f"\nRoom: {self.room_number} \nRoom Type: {self.room_type} \nBalcony: {self.balcony} \nAC: {self.ac} \nRoom Service: {self.room_service} \nPrice: {self.price} \nStatus: {status}"


class Hotel:
    '''
    Hotel class to manage guests, staff, and rooms
    '''
    def __init__(self, name):
        self.name = name
        self.rooms = []  
        self.guests = []  
        self.staff = []  

    def add_room(self, room):
        '''Add rooms to the hotel'''
        self.rooms.append(room)

    def add_guest(self, guest):
        '''
        Add a guest and assign a room if available
        '''
        self.guests.append(guest)

        # Assign guest to a room using the given condition
        for room in self.rooms:
            if room.room_number == guest.room_number:
                room.occupied = True
                break

    def add_staff(self, staff):
        '''Add staff to the hotel'''
        self.staff.append(staff)

    def display_rooms(self):
        print(f"Rooms in {self.name}:")
        for room in self.rooms:
            print(room)
            print("----------------------------------------------\n")

    def display_guests(self):
        print(f"Guests in {self.name}:")
        for guest in self.guests:
            print(guest)
            print("----------------------------------------------\n")

    def display_staff(self):
        print(f"Staff in {self.name}:")
        for staff in self.staff:
            print(staff)
            print("----------------------------------------------\n")





    
    

    


# p1 = Person("bhavit", 123456,"Banglore india")
# print(p1)        
# print(p1.name)