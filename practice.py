# str=input("enter the string :")
# if "ing"in str:
#     print(str+"ly")
# else:
#     print(str+"ing")        

# str="computer"
# print(str)
# print(str[-1:]+str[1:-1]+str[:1])

# s="sheetal.java"
# print(s[-5:])

# water=int(input("enter the number : "))
# if water<1:
#     print("needs to feel")
# elif water>=1 and water<=10:
#     print("no needto feel water")
# elif water>10:
#     print("overflow")        

# user=12
# a=int(input("enter the number"))
# if a>user:
#     print("extra girls=",a-user)
# elif a<user:
#     print("we need girls=",user-a)
# else:
#     print("nothing")        

str=input("enter the charater :")
if "ly"in str:
    print(str[:-2]+"ing")
elif "ing"in str:
    print(str[:-3]+"ly")
else:
    print(str+"ing"+"ly")        