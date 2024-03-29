# Lists: ordered, mutable, allows duplicate eliments
mylist = ["banana", "cherry", "apple"]
print(mylist)

mylist2 = [5, True, "apple", "apple"]
print(mylist2)

item = mylist[0]
print(item)

# for in loop to print mylist elements
for i in mylist:
    print(i)
    
if "apple" in mylist:
    print("yes")
else:
    print("no")
    
mylist.append("lemmon")
print(mylist)

mylist.insert(1, "blueberry")
print(mylist)

item = mylist.pop()
print(item)
print(mylist)

item = mylist.remove("cherry")
print(mylist)

mylist = [4, 3, 1, -1, -5, 10]
print(mylist)

new_list = sorted(mylist)
print (mylist)
print(new_list)

mylist = [0] * 5
print(mylist)

mylist2 = [1, 2, 3, 4, 5]

new_list = mylist + mylist2
print(new_list)

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = mylist[1:5]
print(a)

a = mylist[::2]
print(a)

reverse = mylist[::-1]
print(reverse)
list_org = ["banana", "cherry", "apple"]

list_cpy = list_org
print(list_org)

list_cpy.append("lemon")

print(list_cpy)
print(list_org)


# actual copies
list_cpy = list(list_org) 
list_cpy = list_org[:]
list_cpy = list_org.copy()

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = [i * i for i in mylist]

print(mylist)
print(b)