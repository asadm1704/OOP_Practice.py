#i tried this approach by myself and it worked perfectly
num=[0,1,2,3,2,4,0,7,6,7,8,5,0,6,0,]
for i in range(0,len(num)):
    if num[i]==0:
        num.remove(num[i])
        num.append(0)
print(num)
#trying another approach for that 
n=len(num)
temp=[]
for i in range(0,n):
    if num[i]!=0:
        temp.append(num[i]) 
n2=len(temp)
for i in range(0,n2):
    num[i]=temp[i]
for i in range(n2,n):
    num[i]=0
    
#another approach without using extra space
nums = [0, 1, 2, 3, 2, 4, 0, 7, 6, 7, 8, 5, 0, 6, 0]

if len(nums) <= 1:
    print(nums)
else:
    i = 0
    while i < len(nums):
        # Find first zero
        if nums[i] == 0:
            # Find first non-zero after this zero
            j = i + 1
            while j < len(nums):
                if nums[j] != 0:
                    # Swap zero with non-zero
                    nums[i], nums[j] = nums[j], nums[i]
                    break
                j += 1
            
            # If no non-zero found after this zero, we're done
            if j == len(nums):
                break
        i += 1

    print(nums)