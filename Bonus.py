#A company decides to give a bonus to all its
#employees on Diwali. A 5% bonus on salary is
#given to the male workers and 10% bonus on salary
#to the female workers. Write a program to enter the salary of the employee and the sex of the employee.
#If the salary of the employee is less than Rs. 10,000
#then the employee gets an extra 2% bonus on salary.
#Calculate the bonus that has to be given to the
#employee and the salary that the employee will get.
#input
salary=int(input("Enter the salary"))
gender=input("Enter the gender (M-Male/F-Female)")

#process
if gender=="M":
    bonus=5/100*salary
elif gender=="F":
    bonus=10/100*salary

if salary < 10000:
    bonus2=2/100*salary
else:
    bonus2=0
gross_salary=salary+bonus+bonus2

#output
print("Basic pay =",salary)
print("Gender Bonus = ", bonus)
print("salary bonus = ", bonus2)
print("Final Salary in hand= ",gross_salary)
