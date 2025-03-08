
# remove duplicates from  string

test_dict = {'gfg': 10, 'is': 15, 'best': 20, 'for': 10, 'geeks': 20}
print(test_dict.items())
print("ORGINAL _STRING --------",str(test_dict))

temp = []
res = dict()

for key, val in test_dict.items():
    print(key,val)
    
    if val not in temp:
        temp.append(val)
        res[key] = val
    
print(res)