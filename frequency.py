list_items=[10,20,30,40,50]
frequency={}

for item in list_items:
    if item in frequency:
        frequency[item]=frequency[item]+1
    else:
        frequency[item]=1

print("frequency",frequency)


# to take values from user
# list_items=list(map(int,input("enter the values").split()))
# frequency={}

# for item in list_items:
#     if item in frequency:
#         frequency[item]=frequency[item]+1
#     else:
#         frequency[item]=1
# print("frequency",frequency)

