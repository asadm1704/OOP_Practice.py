'''this is a leetcode problem in whic we are given an array 
and we have to find the indexes of two numbers such that they add up to a specific target'''
nums=[1,5,6,7,4,8,9,2,3,0]
target =13
i=0
j=i+1
n=len(nums)
for i in range(0,n-1):
    for j in range (i+1,n):
        if nums[i]+ nums[j] == target:
            print("Indexes are:",[i,j])
            break

# another approach using  hashing dictionary
           


    
        
        