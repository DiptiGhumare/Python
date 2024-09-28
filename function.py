# #user defines
# def hello():
#     print("Hello World")
# hello()
# def addnum():
#     print(10+20+30)
# addnum()


# def hello(fname,lname):
#     print(fname,lname)
# fname="dipti"
# lname="ghumare"
# hello(fname,lname)

# #built in functions max,min,int,float,type,len

# print(max(40,50,30))


n=int(input("enter the number"))
if(n>1):
    for i in range(2,n):
        if n%i==0:
            print(n,"is not prime")
            break
    else:
        print(n)

else:
    print(n,"not prime")
