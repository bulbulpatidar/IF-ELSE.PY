


sale=int(input("enter the seling price"))
buy=int(input("enter the buy price"))
if sale>buy:
    print("profit")
    value=sale -buy
    print(value)
elif sale<buy:
    print("loss") 
    value=buy-sale
    print(value) 
else:
    print("equal")      