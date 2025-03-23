
# given  a  string count the maximum  number of substring 

actual_string = "aabbaaaaaaaccdefaaa"

k = "a"
count = 0
result = []

for char in actual_string:
    if char == k:
        count +=1
    else:
        count = 0
    result.append(count)

max_result = max(result)
print("MAXIMUM NUMBER OF TIMES A IS BEING REPEATED IS" , max_result)