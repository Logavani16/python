r1,r2=map(int,input("").split())
r1=r1 ^ r2
r2=r1 ^ r2
r1=r2 ^ r1
print(r1,r2)
