
# based  on  the  kth value we need to  get that  string

test_list = ["Nearlearn" ,"teaches", "datascience", "Machinelearning","deeplearning","for","learners"]

k = 20
indx = 0 
print("ORGINAL STRING",test_list)


for word in test_list:
    print(word ,len(word))
    if indx + len(word) > k:
        print("index of character at kth position",str(k-indx))
        break
    else:
        indx += len(word)

