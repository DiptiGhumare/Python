def insertion(array):
    length=len(array)
    for i in range(1,length):
        value=array[i]
        j=i-1
        while j>=0 and value<array[j]:
            array[j+1]=array[j]
            j-=1
        array[j+1]=value
    return array
array=list(map(int,input("enter the elements").split()))
print(insertion(array))