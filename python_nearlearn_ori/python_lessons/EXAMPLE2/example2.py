
# Given a list there wil be zeros we need count the occurance of number init 
  


#  12,3,0,0,0,9,0,6,0,0

def count_numbers(arr, number):

    size = len(arr)
    i = 0
    count = 0

    while i < size:
        if number == arr[i]:
            count += 1
            
        i = i + 1
    
    return count


arr = [1,2,0 ,0,0,0,3,2,6,78,96]
num = int(input("ENTER THE NUMBER \n"))

total_count = count_numbers(arr,num)
print(total_count)
