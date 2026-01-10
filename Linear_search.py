num=[1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1]
target =int(input("please enter the number you want to find in the array :"))
count =0
for i in range (0,len(num)):
    if num[i]==target:
        count+=1
if count>0:
    print(f"the number is found in the array  :{count} times")
if count==0:
    print("the number is not found in the array")         
    