totalclass=int(input("enter the total class"))
attendclass=int(input("enter total no of class attend"))
medicalissue=input("enter the medical issue(Y-yes/N-no)")
#process
percentage=attendclass/totalclass*100
print(percentage)
if percentage>=75:
    print("eligible for exam. He got above 75%")
elif percentage<=75 and medicalissue=="y":
    print("eligible for exam")
else:
    print("not eligible")
