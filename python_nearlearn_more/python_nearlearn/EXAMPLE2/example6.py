
# repalce the string  with old and new in  list of strings

# def replace_str(arr,string):
    
#     for i in range(len(arr)):
#         if arr[i] == 'best':
#             arr[i] = string
    
#     return arr


# test_list = ['Gfg', 'is', 'best', 'for', 'Geeks']
# result_list = replace_str(test_list,"worst")
# print(result_list)


def replace_str(arr):
    
    result = [val.replace('best','worst') for val in arr] #  list comprehension  is something we modify the list itself
    return result

test_list = ['Gfg', 'is', 'best', 'for', 'Geeks']
result_list = replace_str(test_list)
print(result_list)