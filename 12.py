r1=int(input())
temp=r1
co=0
while(r1>0):
  p=r1%10
  co=co*10+p
  r1=r1//10
if(temp==co):
  print("yes")
else:
  print("no")
