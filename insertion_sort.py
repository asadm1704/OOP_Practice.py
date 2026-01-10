'''insertion sort algorithm implementation
In insertion sort we build the sorted array one element at a time.
We take one element from the unsorted array and insert it into its correct position in the sorted array.
first we take a key variable in which we store the number of the current index 
then we create a j variable which is equal to i-1 means we place j at the previous index of i
then we compare the key with the elements before it in the sorted array by while loop using and operator if the both conditions are true
are j is greater than or equal to 0 and nums[j] is greater than key
if both conditions are true we shift the element at j to the right by assigning nums[j] to nums[j+1]
then we decrement j by 1
when the while loop ends we place the key at its correct position by assigning key to nums[j+1]
time complexity: O(n^2)
space complexity: O(1)  '''
nums=[3,2,4,6,9,3,6,1]
n = len(nums)
for i in range(1,n):
    key = nums[i]
    j = i - 1
    while j >= 0 and nums[j] > key:
        nums[j + 1] = nums[j]
        j -= 1
    nums[j + 1] = key
print(nums)