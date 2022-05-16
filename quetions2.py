year=int(input("enter the year :-"))
month=int(input("enter the month :-"))
day=int(input("enter the day :-"))
if month>=1 and month<=12:
    if day>=1 and day<=31:
        day=day+1
        print(year,"-",month,"-",day)
    else:
        ("plz enter valid date")
else:
    print("plz enter valid date")            
