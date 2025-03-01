# find prime number in range
start = 10
end = 1000
 
for val in range(start,end):
    for i in range(2,val):
        if val % i == 0:
            break 
    else:
        print(val)