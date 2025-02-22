l = 5
for i in range(1 , l):    
    for j in range(1, l-i):
        print("", end = "")
    for j in range(1, i + 1):
        print("*", end=" ")
    print("\n")
