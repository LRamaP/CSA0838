previous_Reading=int(input("Enter the previous reading"))
current_Reading=int(input("Enter the current reading"))
unit_cons=current_Reading-previous_Reading
print("Unit consumed =",unit_cons)

if unit_cons <150:
    cost=unit_cons*2
elif unit_cons>151 and unit_cons<300:    # if unit>101 <150
    cost=100+(unit_cons-150)*3


print("EB charge = ",cost)
