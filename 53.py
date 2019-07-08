vani=int(input())
swe=0
i=0
while(vani>0):
    i=vani%10
    swe=swe+i
    vani=vani//10
print(swe)
