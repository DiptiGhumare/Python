lower=int(input("enter the lower value"))
upper=int(input("enter the upper value"))
print("Prime number in the given range are:")
for number in range(lower,upper+1):   #1 is necessary because the range stops one number before the upper limit
     if(number>1):   #this check if the current number is greater than 1 prime numbers are greator than 1 have no divisors other than 1 and themselves.
         for i in range(2,number): #iterates over each number in the range from 2 to number .the range function generates a sequence of numbers in the range 2 and number-1 hence we have to give the number greater than 1 than the number till which we want to check
             if(number%i==0):#checks if the curent number in the outer loop is divisible by the current number being evaluated in inner loop .if the remainder is 0 then number is divisible by i and not a prime number.loop is break using break statement.
                 break
         else:# if number is not divisible by i then it prime
             print(number)



