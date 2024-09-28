def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def mul(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2

print("select the operation:\n"
      "1.addition\n"
      "2.subtraction\n"
      "3.multiplication\n"
      "4.Division\n")

choice = int(input("Select the operation 1,2,3,4:"))
num1=int(input("enter the first value:"))
num2=int(input("enter the second value:"))

if choice==1:
    print(num1,"+",num2,"=",add(num1,num2))

elif choice==2:
    print(num1,"-",num2,"=",sub(num1,num2))

elif choice ==3:
    print(num1,"*",num2,"=",mul(num1,num2))

elif choice ==4:
    print(num1,"/",num2,"=",div(num1,num2))

else:
    print("invalid operation")