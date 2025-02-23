

# give a list contning tuple if tuple is empty then filter 




def filter_tuple(arr):
    result = []
    for val in arr:
        if val:
            result.append(val)
    
    return result



arr = [(23,45) , () , (4,5) , (6,7) , (14,6) , ()]
result_list = filter_tuple(arr)
print(arr,"\n")
print("-"*10,"\n")
print(result_list)