def bubble(array):
    length=len(array)
    for i in range(0,length-1):
        for j in range(length-1):
            if array[j]>array[j+1]:
                temp=array[j]
                array[j]=array[j+1]
                array[j+1]=temp
    return array
array=list(map(int,input("enter tge elements").split()))
bubble(array)
print("the bubble sort is",bubble(array))