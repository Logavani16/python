sa1=int(input())
at1=list(map(int,input().split()[:sa1]))
at1.sort()
for i in at1:
  print(i,end=" ")
