# dictionary: key-value pairs, Unordered, Mutable
mydict = {"name": "Max", "age": 28, "city": "New York"}
print(mydict)

mydict2 = dict(name = "Mary", age = 27, city = "Boston")
print(mydict2)

value = mydict["name"]
print(value)

value = mydict["age"]
print(value)

mydict["email"] = "max@xyz.com"
print(mydict)

mydict["email"] = "coolmax@xyz.com"
print(mydict)

del mydict["name"]
print(mydict)

mydict.pop("age")
print(mydict)

mydict.popitem()
print(mydict)

if "name" in mydict:
    print(mydict["lastname"])
    
try:
    print(mydict["name"])
except:
    print("Error")
    
for key in mydict:
    print(key)
    
for key, value in mydict.items():
    print(key, value) 
    
mydict_cpy = mydict
print(mydict_cpy) 

mydict_cpy = dict(mydict)
mydict_cpy["email"] = "max@xyz.com"
print(mydict_cpy)
print(mydict)

mydict.update(mydict2)
print(mydict)

my_dict = {3: 9, 6: 36, 9: 81}
print(my_dict)

value = my_dict[3]
print(value)

# cant use list because they are mutable, only tubles
mytuple = (8, 7)
mydict = {mytuple: 15}

print(mydict)