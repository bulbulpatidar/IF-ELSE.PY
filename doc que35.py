cp=int(input("entrt the cost price:-"))
if cp>100000:
    tax=cp*15/100
    print("total-",cp+tax)
elif cp>500000 and cp<=100000:
    tax=cp*10/100
    print("total-",cp+tax)
elif cp<=50000:
    tax=cp*5/100
    print("total-",cp+tax)
# else:
#     print("not tax")            