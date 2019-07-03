r1=int(input())
summation=0
temper=r1
while temper>0:
   digital=temper%10
   summation += digital**3
   temper//=10
if r1==summation:
   print("yes")
else:
   print("no")
