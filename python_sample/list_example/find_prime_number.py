
# find the prime number

arr1 = [12,23,45,67,89,9,8,5]


def prime_number(arr1):
    prime_list = []
    for val in  arr1:
        if val % val == 0 and val % 2 == 0:
            print('Val is  not prime')
        else:
            prime_list.append(val)

    return prime_list



prime_numbers = prime_number(arr1)
print("PRIME NUMBERS  ", prime_numbers)


