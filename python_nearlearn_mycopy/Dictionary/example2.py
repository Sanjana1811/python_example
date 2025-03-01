Dict1 = {"name":"surya",
         "age":23,
         "location":"banglore",
         "course":["python", "machinelearning"]}


# update function 
print("ORGINAL DICTIONARY-------",Dict1,"\n")


Dict1.update({"bhavit":"AI engineer"})
print(Dict1)


# change values of dictionary 
Dict1["location"] = "Mumbai"

print("CHANGES DICTIONARY \n",Dict1)

# get 
print("GET SPECIFIC KEY VALUE",Dict1.get("name"))
print("GET SPECIFIC KEY VALUE",Dict1["name"])