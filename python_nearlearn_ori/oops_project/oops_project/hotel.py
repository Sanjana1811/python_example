from miniproject import Person , Guest ,Staff ,Room ,Hotel



# Create object for  Hotel class

hotel = Hotel("Gilton")
print(hotel.name)

# adding the rooms
print("******************Assinging the room******************\n")
hotel.add_room(Room(101,"1bed","Garden view" ,"With Ac","with room service" ,"5k/day"))
hotel.add_room(Room(102 ,"2bed","Garden view" ,"With Ac","with room service" ,"3k/day"))
hotel.add_room(Room(103 ,"3bed","sea view" ,"With Ac","with room service" ,"4k/day"))

hotel.display_rooms()

# adding the guest 
hotel.add_guest(Guest("Rudresh" ,1223456,"Banglore India",103))
hotel.add_guest(Guest("Surya" ,1645456,"Mumbai India",102))
hotel.add_guest(Guest("Divya" ,1978456,"Gujrat India",101))

print("*****************Guest Accomodate*****************\n")
hotel.display_rooms()

# print guest 
hotel.display_guests()

# addong the staff to  list 
print("*****************Adding  the Staff *****************\n")
hotel.add_staff(Staff("Mike",34432424,"Thailand" ,"0098","Headchef"))
hotel.add_staff(Staff("Tom",4545345,"Banglore" ,"0055","Manager"))
hotel.add_staff(Staff("Priyanka",34432424,"Gujrat" ,"0078","Receptionist"))
hotel.add_staff(Staff("Albert",78949456,"Goa" ,"0076","Cleaner"))

# displaty staff 
hotel.display_staff()