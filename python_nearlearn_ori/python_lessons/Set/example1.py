thisset = {"apple", "banana", "cherry"}

print(type(thisset))
print("LENGHT ",len(thisset))


thisset2 = {"apple", "banana", "cherry" ,"apple" , "mango"}
print("WILL REMOVE THE DUPLICATES",thisset2)


intersection_set = thisset2.intersection(thisset)
print("INTESECTION---------------->",intersection_set)
print("UNION ----------->" ,thisset.union(thisset2))