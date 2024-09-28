
"""
string=input(("Enter the text: "))
if(string==string[::-1]):
    print("palindrome")
else:
    print("not palindrome")
    """
"""
paindrome using reversed function
text=input("enter the text: ")
rev=reversed(text)
if(list(text)==list(rev)):
    print("palindrome")
else:
    print("not palindrome")

"""
#palindrome using temporary variable

n=int(input("enter the number"))
temp=n
rev=0
while(n>0):
    last=n%10
    rev=rev*10+last
    n=n//10
if(temp==rev):
    print("palindrome")
else:
    print("not palindrome")

    '''In the first iteration of the loop:

last = n % 10 gives last = 123 % 10 = 3
rev = rev * 10 + last gives rev = 0 * 10 + 3 = 3
n = n // 10 gives n = 123 // 10 = 12
In the second iteration:

last = n % 10 gives last = 12 % 10 = 2
rev = rev * 10 + last gives rev = 3 * 10 + 2 = 32
n = n // 10 gives n = 12 // 10 = 1
In the third iteration:

last = n % 10 gives last = 1 % 10 = 1
rev = rev * 10 + last gives rev = 32 * 10 + 1 = 321
n = n // 10 gives n = 1 // 10 = 0
Once n becomes 0, the loop stops because there are no more digits left to process.'''