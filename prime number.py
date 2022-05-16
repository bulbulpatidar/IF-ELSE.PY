n=int(input("enter the number :"))
if n==2 or n==3 or n==5 or n==7 or n==11:
    print("prime number")
elif n%2==0 or n%3==0 or n%5==0 or n%7==0:
    print("not prime number")
else:
    print("prime number")        
