kilometers = float(input("Enter distance in kilomenters: "))

#Conversation factor: 1 kilometers = 0.621371 miles
conversion_factor = 0.621371

miles = kilometers * conversion_factor
print(f"{kilometers} kilometers is equal to {miles} miles")