def are_anagrams(word1,word2):
    word1=word1.lower()
    word2=word2.lower()

    sorted_word1=sorted(word1)
    sorted_word2=sorted(word2)

    return sorted_word1==sorted_word2

word1=input("enter the first word")
word2=input("enter the second word")
print(are_anagrams(word1,word2))


str1=input("enter the first string")
str2=input("enter the second string")

str1=str1.replace(" ","").lower()
str2=str2.replace(" ","").lower()

if len(str1)!=len(str2):
    print(f"string{str1}and string{str2} are not anagrams")
elif sorted(str1)==sorted(str2):
    print(f"string{str1} and string{str2}are anagrams")
else:
    print(f,"string{str1} and string{str2} are not anagrams ")