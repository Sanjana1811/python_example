# given  a  array we need to  find  the maximum  distance betweeen two occurance 
# do it using dictionary 
#  arr = [1,1,2,2,2,1]

# 0
# 5  (5 -0)

# 2-----> 3 ,4 (4-3) = 1

dist = {}
dist_1 = {}
res = 0

arr = [1,1,2,2,2,1]  # 0 5  max - min 5 -0 =4



# dictionary for storing the first occurence
for i in  range(len(arr)):
    if arr[i] not in dist_1:
        dist_1[arr[i]] = i

# dictionary for storing the the last occurence
for i in range(len(arr)):
    dist[arr[i]] = i


print("MIN",dist_1)
print("MAX",dist)   

dist_for_one = dist[1] - dist_1[1] 
dist_for_two = dist[2] - dist_1[2]


print("DISTANCE FOR ONE IS", dist_for_one)
print("DISTANCE FOR TWO IS", dist_for_two)


