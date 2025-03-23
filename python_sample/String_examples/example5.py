# given a two  string  check wether these are anagrams or not 

s1 = "listen"
s2 = "silent"


# # remove duplicates 
char1 = set(s1)
char2 = set(s2)

print("String 1", char1)
print("String 2",char2)

if char1 == char2:
    print("YES ITS AN ANAGRAM-----")

else:
    print("NO ITS NOT ANAGRAM")


# # # remove duplicates 
# char1 = s1.split()
# char2 = s2.split()

# char1.sort()
# char2.sort()

# print("String 1", char1)
# print("String 2",char2)

# if char1 == char2:
#     print("YES ITS AN ANAGRAM-----")

# else:
#     print("NO ITS NOT ANAGRAM")