my_set={2,6,5,4,3,7,8,9}
print(my_set)

set={1,1.0,"helloworlds"}   #not allow duplicates it not support indexing
print(set)

#add()   to add single item
my_set={2,6,5,4,3,7,8,9}
my_set.add(3)
print(my_set)

#update()  to add multiple items    write ithems inside list for update
my_set={2,6,5,4,3,7,8,9}
my_set.update([10,11,12])
print(my_set)

#remove
my_set={2,6,5,4,3,7,8,9}
my_set.remove(2)
print(my_set)


#set operation
#union()   set of all elements in both   avoid common elements print ones  it joins both the sets
a={1,2,3,4,5,6}
b={7,8,9,1,2,5}
print(a|b)

#intersection  elements that are common
a={1,2,3,4,5,6}
b={7,8,9,1,2,5}
print(a&b)

#access items
my_set={2,6,5,4,3,7,8,9}
for x in my_set:
    print(x)

print(2 in my_set)