

# lambda expression 

import math
# summation of two  numbers 

add = lambda a ,b : a + b
print("Addition",add(5,10))

mult = lambda a ,b : a * b
print("mult",mult(5,10))

division = lambda a ,b : a /b
print("mult",division(5,10))

 

quadrtic1  = lambda a,b,c : -(math.sqrt(b*b - 4 * a *c )/2 *a)
quadrtic2  = lambda a,b,c : (math.sqrt(b*b - 4 * a *c )/2 *a) 


print("Quadratic 1", quadrtic1(2,34,3))
print("Quadratic 2", quadrtic2(2,34,3))