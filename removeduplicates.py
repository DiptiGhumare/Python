list_items=list(map(int,input("enter the values").split()))
print("the items before removing dublicates",list_items)
unique_values=list(set(list_items))
print(unique_values)