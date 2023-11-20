x=int(input("Roll number of student:"))
y=input("Name of the student:")
phy=int(input("Marks in Physics:"))
chem=int(input("Marks in Chemistry:"))
math=int(input("Marks in Mathematics:"))
tot=phy+chem+math
print("Total marks of",y,'is:',tot)
avg=tot/3
print("Average marks of",y,'is:',avg)
