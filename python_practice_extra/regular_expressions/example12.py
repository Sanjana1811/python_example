# The Match object has properties and methods used to retrieve information about the search, and the result:

# .span() returns a tuple containing the start-, and end positions of the match.
# .string returns the string passed into the function
# .group() returns the part of the string where there was a match

import re

#Search for an upper case "S" character in the beginning of a word, and print its position:
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())


#The string property returns the search string:


txt1 = "The rain in Spain"
x1 = re.search(r"\bS\w+", txt1)
print(x1.string)

#Search for an upper case "S" character in the beginning of a word, and print the word:


txt2 = "The rain in Spain"
x2 = re.search(r"\bS\w+", txt2)
print(x2.group())