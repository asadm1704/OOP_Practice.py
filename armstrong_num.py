n=153
num=n
total=0
count=0
while n>0:
    count +=1
while n>0:
    ld=num %10
    total=total +(ld**count)
    num =num //10 
if total==n:
    print(f"{n} is an Armstrong number")    
else:
    print(f"{n} is not an Armstrong number") 
