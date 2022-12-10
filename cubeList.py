#given a range, create three lists, list1 should contain numbers,
#list2 contain squares of the numbers
#list3 contain cube of the numbers

List1=[]
List2=[]
List3=[]

lower=int(input("enter the lower limit"))
upper=int(input("enter the upper limit"))

for i in range(lower,upper):#5,6,7,8,9
    List1.append(i)
    List2.append(i*i)   #i**2
    List3.append(i*i*i) #i**3

print("list contains numbers :", List1)
print("list contains square of numbers :", List2)
print("list contains cube of numbers :", List3)

    




    
