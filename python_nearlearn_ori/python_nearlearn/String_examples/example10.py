a = [[1, 2, 3], 
     [4, 5, 6], 
     [7, 8, 9]]

b = [[9, 8, 7], 
     [6, 5, 4], 
     [3, 2, 1]]

res = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


rows = (len(a))
coloumns = len(a[0])

for i in range(rows):
    for j in range(coloumns):
        for k in range(rows):
            print(i,k ,(k,j))
            res[i][j] += a[i][k]  * b[k][j]



for r in res:
    print(r)