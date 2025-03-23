

def even(n):
    return n % 2 == 0

def odd(n):
    return n % 2 != 0


val = [2,3,4,5,6,7,8,10]

even_number = filter(even,val)
odd_number = filter(odd,val)

print("even",list(even_number))
print("odd" ,list(odd_number))
