#Write a python program to calculate the salary of an employee
#given his basic pay (to be entered by the user) HRA=10% of basic pay.
#TA=5% of basic pay. Define HRA and TA as constants and
#use them to calculate the salary of the employee

#input
basicPay=int(input("enter the basic pay"))

#process
HRA=10/100*basicPay    # HRA,hra,HRa
TA=5/100*basicPay
Salary=basicPay+HRA+TA

#output
print("Basic pay =",basicPay)
print("House rent allowance = ", HRA)
print("Travelling allowance = ", TA)
print("Salary = ",Salary)
