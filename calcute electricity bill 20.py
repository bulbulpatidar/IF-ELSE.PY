


# calculate electricity Bill
# first 50 unit rs 0.50/unit
# for next 100 unit rs 0.75/unit
# for next 100 unit rs 1.20/unit
# for unit above 250 rs 1.50/unit
# additional surcharge of 20% is added bill

unit=int(input("enter the unit:-"))
if unit<=50:
    rs=unit*0.50
    print("electricity bill-",rs)
    surcharge=rs*20/100
    print("surcharge-",surcharge)
    total_bill=rs+surcharge
    print("total bill-",total_bill)
elif unit<=150:
    rs=unit*0.75
    print("electricity bill-",rs)  
    surcharge=rs*20/100
    print("surcharge-",surcharge)  
    total_bill=rs+surcharge
    print("total bill-",total_bill)
elif unit<=250:
    rs=unit*1.20
    print("electricity bill-",rs)   
    surcharge=rs*20/100
    print("surcharge-",surcharge) 
    total_bill=rs+surcharge
    print("total bill-",total_bill)
elif unit>250:
    rs=unit*1.50
    print("electricity bill-",rs)
    surcharge=rs*20/100
    print("surcharge-",surcharge)   
    total_bill =rs+surcharge
    print("total bill-",total_bill)