'''in bubble sort we repeatedly swap the adjacent elements if they are in wrong order.
means we push the largest unsorted element to its correct position in each iteration.
or to the end od the array 
quickly we can say that in each iteration the largest unsorted element bubbles up to its correct position.
Time Complexity: O(n^2)
Space Complexity: O(1)
we will place i at the n-2 th index and j at 0th index
then we will compare j and j+1 th index if j is greater than j+1 then we will swap them
we will repeat this process until the array is sorted.'''
nums=[1,2,3,4,5,6,7,8,9]
n=len(nums)
for i in range (n-2,-1,-1):
    is_sorted = True
    for j in range(0,i+1):
        if nums[j]>nums[j+1]:
            nums[j],nums[j+1] = nums[j+1],nums[j]
            is_sorted = False
    if is_sorted == True:
        print("array is sorted")
        break
print(nums)