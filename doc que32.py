unit=int(input("enter the unit:-"))
if unit<=100:
    print("no charge")
elif unit<=200:
    print(5*unit)
elif unit>200:
    print(10*unit) 
else:
    print("nothing")           