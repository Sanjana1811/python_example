def remove_multi(arr, num):
    size=len(arr)
    filter_list = []
    for val in arr:
        if val != num:
            filter_list.append(val)
        else:
            pass

    return filter_list

arr = [1, 2,3,4,5,6,6,6,7,6]
num = int((input('enter the number you want to remove from list : ')))

filter_list =remove_multi(arr, num)
print(filter_list)


