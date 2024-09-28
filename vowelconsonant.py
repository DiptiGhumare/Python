# 

string = input("enter the string")
string = string.lower()

vowel = 0
consonant = 0

vowels_found = []
consonants_found = []

vowels ='aeiou'

for char in string:
    if char in vowels:
        vowel+=1
        vowels_found.append(char)
    elif char.isalpha():
        consonant+=1
        consonants_found.append(char)

print("vowels",vowel)
print("consonant",consonant)

print("vowels_found are",vowels_found)
print("consonants found are",consonants_found)


string = input("enter the string")
string=string.lower()

vowels=0
vowels_found=[]

vowel='aeiou'

for char in string:
    if char in vowel:
        vowels +=1
        vowels_found.append(char)

print("vowels found",vowels_found)
print("vowels",vowels)


n=int(input("enter the year"))
if(n % 4 ==0 | n % 400 ==0 & n % 100!=0):
    print("year is leap")
else:
    print("year is not leap")
