A=[10,45,67,89,78,45]
print(A)

#list allows duplicates
list=["apple","banana","cherry","apple"]
print(list)

#length of list,length starts from 1
print(len(list))

#list items can of any data type
list1=["apple","banana","cherry","apple"]
list2=[2,5,6,7,8,9]
list3=[True,False,False]
print(list1)
print(list2)
print(list3)

#list can contain different data types
thislist=["apple",23,True,78,"male"]
print(thislist)

#accessing list items
thislist=["apple",23,True,78,"male"]
print(thislist[0])
print(len(thislist))

#nested list
nest_list=["hello",[1,2,3]]
print(nest_list)
print(nest_list[1])
print(nest_list[1][2])

#negative indexing
a=[1,2,3,4,5,6]
print(a[-1])

#list methods
#append() used to add element in last of the list
fruit = ["apple","mango","grapes"]
fruit.append("banana")
print(fruit)

#extend() use to add one list in another list 
lang = ["english","hindi"]
lang1=["french","germany"]
lang.extend(lang1)
print(lang)

#its not mandotory that we can only extent list we can also add tuple,set
lang = ["english","hindi"]
points=(1,2,5,9)
lang.extend(points)
print(lang)

#index()   tells the position of element

lang = ["english","hindi","french","germany","marathi"]
print(lang.index("hindi"))

#insert()   can insert elements at any position
lang = ["english","hindi","french","germany","marathi"]
lang.insert(0,"malayam")
print(lang)

#count()   count the list item that how many times it occurs
list2=[1,4,5,6,7,3,3,4,6,7,8,7,2,1,1,1,4]
print(list2.count(1))

#remove()     remove element by specify name of particular element
lang = ["english","hindi","french","germany","marathi"]
lang.remove("germany")
print(lang)

#pop() remove element by there index
lang = ["english","hindi","french","germany","marathi"]
lang.pop(1)
print(lang)

#if we cant give index in pop by default it remove last element
lang = ["english","hindi","french","germany","marathi"]
lang.pop()
print(lang)

#reverse()    reverse the order of list
lang = ["english","hindi","french","germany","marathi"]
lang.reverse()
print(lang)

#sort()    sort the list in asending order

lang = ["english","hindi","french","germany","marathi"]
lang.sort()
print(lang)

list3=[1,6,7,4,5,6,8,9,34,87,6,5,45,3]
list3.sort()
print(list3)

#sort(reverse=True)     sort in decending order
list3=[1,6,7,4,5,6,8,9,34,87,6,5,45,3]
list3.sort(reverse=True)
print(list3)