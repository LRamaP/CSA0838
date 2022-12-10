#pgm to give discount if purchase is above 2000
amt=int(input("enter the purchase amount"))
if (amt > 2000):
    amt= amt-(amt*20/100)
elif (amt > 1000):
    amt= amt-(amt*10/100)
else:
    amt=amt-(amt*5/100)
print("final amount is ",amt)
