import  re 

# txt = "The rain in Spain"

# result = re.findall("Spain",txt)
# print(result)

string = "Hello bhavit how are you"
pattern = r"World!$"

match = re.search(pattern, string)
if match:
    print("Match found!")
else:
    print("Match not found.")