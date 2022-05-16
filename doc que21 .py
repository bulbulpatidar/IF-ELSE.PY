cost=int(input("enter the price:-"))
if cost>=1000:
    cost=cost-cost*10/100
    print(" discount price",cost)
