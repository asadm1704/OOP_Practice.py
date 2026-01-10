#method 1
nums =[10,20,30,40,-90,2,4,5,6,23,56,88,1]
largest =nums[0]
second_largest =nums[0]


for i in range(1,len(nums)):
    #largest= max(largest,nums[i])
    if nums[i] >largest:
        largest=nums[i]
        
     #second largest   
for i in range(1,len(nums)):
    if nums[i] >second_largest and nums[i] != largest:
        second_largest=nums[i]  
        
         
print("The largest number is:",largest)
print("The second largest number is:",second_largest)


# second method is an optimal approach we just update the second largest when we find a new largest
#and place the previous largest to second largest
largst=float('-inf')
second_largst=float('-inf')
for i in range(len(nums)):
    if nums[i]>largst:
        second_largst=largst
        largst=nums[i]
    elif nums[i]>second_largst and nums[i]!=largst:
        second_largst=nums[i]
print("The largest number is:",largst)
print("The second largest number is:",second_largst)
