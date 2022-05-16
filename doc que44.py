a=int(input("enter the number"))
b=int(input("enter the number"))
c=int(input("enter the number"))
if a>b and a<c or a<b and a>c:
    print("2nd largest is a:-",a)
elif b>a and b<c or b<a and b>c:
    print("2nd largest is b:-",b)
elif c>a and c<b or c<a and c>b:
    print("2nd largest is c:-",c) 
else:
    print("unvalid")           
