


#  given  an  two  array check  whether  the two arrays are equal or not 
# create the array  from  the user it self
# then compare 


def comparasion():
    size = 5
    arr1 = []
    arr2 = []

    for i in range(size):
        val = int(input(f"ENTER A ELEMENT FOR 1 ARRAY:{i} \n"))
        arr1.append(val)
    
    for i in range(size):
        val = int(input(f"ENTER A ELEMENT 2 ARRAY: {i} \n"))
        arr2.append(val)

    print(arr1)
    print(arr2)

    arr1.sort()
    arr2.sort()

    print(arr1)
    print(arr2)

    if arr1 == arr2:
        return True
    else:
        return False


resutlt = comparasion()
print(resutlt)

