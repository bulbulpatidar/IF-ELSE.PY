day=int(input("entr the day of number:-"))
if day<=5:
    chrge=day*2
    print("charge for librarary:-",chrge)
elif day>=6 and day<=10:
    chrge=day*3
    print("charge for library:-",chrge)
elif day>10 and day<=15:
    chrge=day*4
    print("chrge for libraray:-",chrge)
elif day>15:
    chrge=day*5
    print("charge for libraray:-",chrge) 
else:
    print("nothing")       
