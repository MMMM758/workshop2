dict1 = {"name": "Atitaya", "age": "20"}
dict2 = {"name": "Atitaya", "age": "20"}
dict3 = dict1

print(dict1 is dict3)
# Output : True
print(dict1 is dict2)
# Output : False
print(dict1 == dict2)
# Output : True