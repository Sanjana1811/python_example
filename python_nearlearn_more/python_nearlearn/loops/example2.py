a = [23,24,25,26,34,56,78,98,123]

print("ORGINAL LIST", a)
size = len(a)
print("SIZE",size)
# for loop intializtion 

for i in range(0,size,2): # start , end ,step
    print("ITERATION", i ,a[i])