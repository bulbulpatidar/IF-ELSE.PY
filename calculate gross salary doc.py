basic_salary=int(input("enter the basic salary"))
if basic_salary<=10000:
    gross_salary=basic_salary+basic_salary*20/100+basic_salary*80/100
    print("grosssalary:-",gross_salary)
elif basic_salary<=20000:
    gross_salary=basic_salary+basic_salary*25/100+basic_salary*90/100
    print("grosssalary:-",gross_salary)
elif basic_salary>20000:
    gross_salary=basic_salary+basic_salary*30/100+basic_salary*95/100
    print("grosssalary:-",gross_salary)    
else:
    print("nothing")    
