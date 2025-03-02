path ="C:\\Users\\s_ara\\python_examples\\python_practice_extra\\Files\\file_content.txt"
file = open(path, "r")
content = file.read()
print(content)
file.close()

# read binary 
file_1 = open(path, "rb")
content_1 = file_1.read()
print(content_1)
file_1.close()


