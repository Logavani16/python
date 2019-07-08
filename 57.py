r1,r2=map(int,input().split())
vani=list(map(int,input().split()[:r1]))
swe=0
for i in vani:
   if(i==r2):
      swe=swe+1
print(swe)
