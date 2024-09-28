num=int(input("enter the number"))
sum=0
while(num>0):
    value=num%10
    sum=sum+value
    num=num//10

print("sum of digits",sum)

a=int(input("enter the number"))
b=int(input("enter the number"))

print(f"before swapping a={a} and b={b}")

a=a+b
b=a-b
a=a-b

print(f"after swapping a={a} and b={b}")