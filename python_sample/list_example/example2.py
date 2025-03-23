


# 234  234 - 23 - 2

# taking input from user 

number = int(input("Enter the Number you  want------ \n"))

temp = number

sum = 0

while  temp > 0:
    digit = temp % 10 # retrun  the remainder 
    sum = sum + digit**3
    temp = temp // 10 # //  floor divsion  return  the  updated number



if sum == number:
    print("YES ITS A ARMSTRONG NUMBER")
else:
    print("NO ITS  NOT A ARM STRONG NUMBER")


