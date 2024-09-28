
def prime(a):
    if a>1:
        for i in range(2,int(a/2)+1):
            if a%i==0:
                print(a,"is not prime")
                break
        else:
            print(a,"is prime")
    else:
        print(a,"not prime")
a=int(input("enter the number"))
prime(a)