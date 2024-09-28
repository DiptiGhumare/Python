def binary(list,key):
    s=0
    e=len(list)-1
    while(s<=e):
        mid=(s+e)//2
        if list[mid]==key:
            return mid
        elif list[mid]>key:
            e=mid-1
        else:
            s=mid+1
    return -1

list=list(map(int,input("enter the number").split()))
key=int(input("enter the number"))
res=binary(list,key)
if(res!=-1):
    print("element found")
else:
    print("element not found")
    

