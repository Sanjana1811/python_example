#  given a string  print  the even number of string 


def even_number_of_string(strings):
    strings = strings.split()
    print(strings)
    for a in  strings:
        if len(a) % 2 == 0:
            print("EVEN LENGTH---- ",len(a) ,a)



n = input("Enter a  string \n")
result = even_number_of_string(n)