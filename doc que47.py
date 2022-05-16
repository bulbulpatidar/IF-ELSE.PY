month=input("enter the month:-")
day=int(input("enter the day:-"))
if month=="december" and day==31 or month=="january" and day==31 or month=="february" and day==28:
    print("season is winter")
elif month=="march" and day==31 or month=="april" and day==30 or month=="may" and day==31:
    print("season is spring")
elif month=="june" and day==30 or month=="july" and day==31 or month=="august" and day==31:
    print("season is summer")  
elif month=="september" and day==30 or month=="octomber" and day==31 or month=="november" and day==30:
    print("seoson is autum")    
else:
    print("nothing")       
