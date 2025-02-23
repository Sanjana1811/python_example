

# given an array  if 0  are there then  remove the 0  from the list 
# dont use any inbuilt function 


def filter_num(arr,num):
    size = len(arr)
    filter_list = []
    for i,val in enumerate(arr):
        if val != num:
            filter_list.append(val)
            # filter_list[i] = val 
            # filter_list = [if ]

        else:
            pass
    
    return filter_list


arr = [1,2,2,2,2,45,67,89]
num = int(input("ENTER THE NUM YOU WANT TO FILTER \n"))

filter_list = filter_num(arr,num)
print(filter_list)



