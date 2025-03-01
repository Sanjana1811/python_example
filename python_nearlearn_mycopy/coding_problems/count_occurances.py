def count_numbers(arr, number):
    size = len(arr)
    i = 0
    count = 0

    while i < size:
        if number == arr[i]:
            count +=1
        i = i + 1
    return count

arr = [ 12, 3, 4, 0, 5, 4, 6, 0]
num = int(input('Enter the number whose multiple occrances need to be checked : ' ))
total_count = count_numbers(arr, num)
print(total_count)