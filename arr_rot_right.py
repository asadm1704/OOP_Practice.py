#rotate an array to the right by one position
nums=[1,2,3,5,4,3,2,5,75,43,6,3,234,56,2]
n=len(nums)
nums[:]=nums[-1:] + nums[:n-1] #[:] is used to stop making new list and just modify the existing one
print(nums) 
#without slicing we can do it like this
temp=nums[-1]
for i in range(n-2,0,-1):
    nums[i+1]=nums[i]
nums[0]=temp
print(nums)


#rotate an array by k positions to the right
num=[1,2,3,5,4,3,2,5,75,43,6,3,234,56,2]
k=15
k=k%n #in case k is greater than n
for i in range(0,k):
    e=num.pop() #removes the last element and returns it
    num.insert(0,e) #inserts the element at index 0
print(num)