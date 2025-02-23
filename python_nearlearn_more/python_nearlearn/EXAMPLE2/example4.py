# given a list of element there will 0 


def  push_zero_to_last(arr,num):
    size = len(arr)
    result = []

    for val in arr:
        if val != num:
            result.append(val)
        
    for val in arr:
        if val == 0:
            result.append(val)
    return result




arr = [1,2,0,0,0,7,8,0,6,9]
new_list = push_zero_to_last(arr,0)
print(new_list)