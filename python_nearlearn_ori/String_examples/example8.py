# given a  problem find vowels in  the  string 

string_1 = "NearlearnDatascience"
vowels = 'aieou'

string_1 = string_1.lower()
print(string_1)


#  creating set for two  string
string1_set = set(string_1)
string2_set = set(vowels)

print(string1_set, "\n")
print(string2_set,"\n")

if  string2_set.issubset(string1_set):
    print("True")
else:
    print("False")