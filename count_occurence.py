def occurence(string,character):
    string=string.lower()
    character=character.lower()

    count=string.count(character)
    return count

s=input("enter the string:")
ch=input("enter the character")
print(f"the character '{ch}' appers {occurence(s,ch)} times in string")



