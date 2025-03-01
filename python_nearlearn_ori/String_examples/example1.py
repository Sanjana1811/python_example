
# given a string  there are spaces in it we need  to remove the spaces 



def remove_spaces(string_list):
    # list comprehension 
    li = [" ".join(val.split()) for val in  string_list]
    return li 



string_list = ["hello   world", "  How are  you doing", " some  spaces"]
print(" ORIGINAL LIST ----------",string_list)
string_li = remove_spaces(string_list)
print("REMOVED SPACES LIST" ,string_li)

