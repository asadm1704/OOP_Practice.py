'''In selection we select the smallest element from the unsorted
part of the array and swap it with the first element of the unsorted part.
We repeat this process for all elements in the array.
Time Complexity: O(n^2)
Space Complexity: O(1)'''

nums=[1,2,3,4,3,2,1,7,9,6,4,2,1,4,6]
def selection_sort(nums):
    n =len(nums)
    for i in range(n):
        min_index =i
        for j in range(i+1,n):
            if nums[j]<nums[min_index]:
                min_index = j
        nums[i],nums[min_index] = nums[min_index],nums[i]
    return nums
print(selection_sort(nums))