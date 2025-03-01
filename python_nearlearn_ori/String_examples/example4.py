
import string

string_a = "Hi  this  is Nearlearn  teaching Machine learning and  deeplearnig"

b = set(string_a.lower())
c = set(string.ascii_lowercase)

print(" ORGINAL STRING-----", b)
print("DUPLICATE STRING ----",c)


res = b <= c
print("RESULT ------",res)

