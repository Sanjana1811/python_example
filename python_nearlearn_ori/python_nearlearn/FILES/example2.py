


path = "D:\python_nearlearn\FILES\hello3.txt"

# appending something to file
file = open(path,"a")
for i in range(4):
    cont_to_write = input("Enter somenthing \n")
    cont_to_write = bytes(cont_to_write.encode("utf-8"))
    content = file.write(f"{cont_to_write} \n")
# print(content)
file.close()