def move_zero_last(arr):
   size=len(arr)
   collect_zero = []
 
   for val in arr:
      if val == 0:
         collect_zero.append(val)
        #  arr.pop(val)
    #   arr.extend(collect_zero)

   return arr

arr = [1, 2, 0, 4, 5, 0, 0, 5, 6, 0, 7]
result = move_zero_last(arr)
print(result)