#tuple: ordered, immutable, allows duplicate elements
mytuple = "Max", 28, "Boston"
print(mytuple)

mytuple = tuple(["Max", 28, "Boston"])
print(mytuple)

item = mytuple[0]
print(item)

for i in mytuple:
    print(i)
    
if "Max" in mytuple:
     print("yes")
else:
     print("no")  
     
my_tuple = 'a', 'p', 'p', 'l', 'e'

print(my_tuple.count('p'))

print(my_tuple.index('p'))

my_list = list(my_tuple)
print(my_list)

my_tuple2 = tuple(my_list)
print(my_tuple2)

a = (1, 2, 3, 4, 5, 6, 7, 8, 9)

b = a[2:5]
print(b)

b = a[::-1]
print(b)

my_tuple = "Max", 28, "Boston"

name, age, city = my_tuple
print(name)
print(age)
print(city)

my_tuple = (0, 1, 2, 3, 4)

i1, *i2, i3 = my_tuple

print(i1)
print(i3)
print(i2)

import sys
import timeit
my_list = [0, 1, 2, "hello", True]
my_tuple = (0, 1, 2, "hello", True)
print(sys.getsizeof(my_list), "bytes")
print(sys.getsizeof(my_tuple), "bytes")

print(timeit.timeit(stmt = "[0, 1, 2, 3, 4, 5]", number = 1000000))
print(timeit.timeit(stmt = "(0, 1, 2, 3, 4, 5)", number = 1000000))

