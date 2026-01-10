nums =[1,1,0,0,1,1,1,0,0,1,1,1,1]
def check_max(nums):
    maximum_times=0
    n=len(nums)
    for i  in range(0,n):
        if nums[i]==1:
            count=0
            for j in range(i,n):
                if nums[j]==1:
                    count+=1
                else:
                    break
            if count>maximum_times:
                maximum_times=count
    return maximum_times
result=check_max(nums)
print("Maximum consecutive 1's are:",result)
      
      #another approach      
            
nums1 =[1,1,0,0,1,1,1,0,0,1,1,1,1]
max1=0
count=0
for i in range(0,len(nums1)):
    if nums1[i]==1:
        count+=1
    else:
        max1=max(max1,count)
        count=0
returned_max=max(max1,count)  # to handle the case when array ends with 1
print("Maximum consecutive 1's are:",returned_max)