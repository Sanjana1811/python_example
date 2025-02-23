a = [10, 20, 4, 45, 99]
 
max1 = 0 
max2 = 0
 
for val in  a:
    if val > max1:
        print("INSIDE FIRST IF")
        max2 = max1 
        max1 = val
    # this is redunant not needed 
    if val > max2 and val != max1:
        print("INSIDE SECOND IF")
        max2 = val
 
print(max1,max2)