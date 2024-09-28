def selection(array):
    length=len(array)
    for i in range(length-1):
        minindex=i
        for j in range(i+1,length):
            if array[j]<array[minindex]:
                minindex=j
        temp=array[i]
        array[i]=array[minindex]
        array[minindex]=temp
    return array
input=input("enter the element")
array=list(map(int,input.split()))
selection(array)
print("selection sort:",selection(array))
