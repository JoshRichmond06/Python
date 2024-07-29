# Sets: unordered, mutable, no duplicates
myset = {1, 2, 3, 1, 2}
print(myset)

myset = set([1, 2, 3])
print(myset)

myset = set("hello")    #use to see amount of individual character/chars/ints etc.
print(myset)
myset = {}
print(type(myset))

myset = set()
print(type(myset))

myset.add(1)
myset.add(2)
myset.add(3)
print(myset)

myset.remove(3)
print(myset)

myset.discard(2)
print(myset)

myset.clear()
print(myset)

myset.add(1)
myset.add(2)
myset.pop()
print(myset)

for x in myset:
    print(x)
    
if 2 in myset:
    print("yes")
    
