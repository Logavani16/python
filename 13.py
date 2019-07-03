r1 =int(input())
if (r1>1):   
   for i in range(2, r1//2):   
       if (r1 %i) == 0: 
           print("no")
           break
   else: 
       print("yes") 
else: 
   print("no") 
