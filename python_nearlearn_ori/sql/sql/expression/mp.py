

val = ['2','3','4','6','7','8','9']
print(val)
print(type(val))
print("\n")

res = map(float ,val)
print(list(res))

a = [1, 2, 3, 4]

res = list(map(lambda x: x ** 2, a))
print(res)