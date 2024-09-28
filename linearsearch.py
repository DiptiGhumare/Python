def linear(array,key,n):
    for i in range(0,n):
        if array[i]==key:
            return i
    return -1
array=list(map(int,input("enter the elements").split()))
key=int(input("enter the key"))
n=len(array)
res=linear(array,key,n)
if res==-1:
    print("element not found")
else:
    print(f"element found {res}")

