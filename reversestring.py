"""
text="hello python"[::-1]
print(text)c
"""
"""
#reverse string using function
def reverse_string(str):
    str=str[::-1]
    return str
string=input("enter the string")
print("original string",string)
print("reverse string",reverse_string(string))

"""
#reverse the string using for loop

def reverse_string(string):
    str1=" "
    for i in string:
        str1=i+str1
    return str1
string="hello"
print("original string",string)
print("reverse string",reverse_string(string))
    

