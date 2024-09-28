# list_items = [80,90,100,30,20]
# large = list_items[0]
# small = list_items[0]

# for i in list_items:
#     if i > large:
#         large = i
#     if i < small:
#         small = i

# print("Largest item",large)
# print("smallest item",small)
    
user_input = input("Enter the values")
list_items = list(map(int,user_input.split()))

small = list_items[0]
large = list_items[0]
for i in list_items:
    if i>large:
        large = i
    if i < small:
        small = i
print("largest item",large)
print("smallest item",small)


