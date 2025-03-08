
path = "D:\python_nearlearn\FILES\hello3.txt"

# reading content in  files
# file = open(path,"r")
# content = file.read()
# print(content)
# file.close()


file = open(path,"rb")
content = file.read()
print(content)
file.close()