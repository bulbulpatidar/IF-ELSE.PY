age=int(input("enter the age"))
sex=(input("enter the sex"))
if age>=18 and age<30:
    if sex=="m":
        print("wage is 700")
    elif sex=="f":
        print("wage is 750")
    else:
        print("not allowed to work")
elif age>=30 and age<=40:
    if sex=="m":
        print("wage is 800")
    elif sex=="f":
        print("wage is 850")
    else:
        print("not allowed to work")
else:
    print("approprivate age")        