
n = 5
for i in range(1 , n):    
    for j in range(1, n-i):
        print("  ", end = "")
    for j in range(1, i + 1):
        print("*", end=" ")
    print("\n")
