r1=input()
r2=0
for i in range(len(r1)):
  if(r1[i].isdigit() or r1[i].isalpha() or r1[i]==(" ")):
    continue
  else:
    r2+=1
print(r2)
