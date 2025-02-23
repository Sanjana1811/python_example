
#  fibonaci  series 


import time


def fibonacci_series():
    num = int(input("ENTER A  NUMBER \n"))

    n1 = 0
    n2 = 1
    n_term = 0
    print(n1)
    print(n2)

    for i in range(num):
        n_term = n1 + n2 
        n1 = n2 # second last term make as first
        n2 = n_term # nth term should become the  second term
        print(n_term)
        time.sleep(2)

fibonacci_series()