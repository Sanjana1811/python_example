# given an  Dictionar it will  contains a key value pairs
# based on the prefix  you need to get the value
# by srisandhya

dictionary = {"tough":234,
              "machinelearning":3,
              "mac":160,
              "deeplearning":3,
              "deepseek":'LLM'}


print(dictionary)


result = []
pref = "deep"

for key,val in  dictionary.items():
    #  if key.startswith(pref):
    #     print(dictionary.get(key))
    
    result.append(key)

for val in result:
    if val.startswith(pref):
        print(dictionary.get(val))

