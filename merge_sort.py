'''Hi this tutorial is going to be on merge sort algorithm in python.
Merge sort is a divide and conquer algorithm that divides the input array into two halves,
calls itself for the two halves, and then merges the two sorted halves.
The merge() function is used for merging two halves.
The merge(arr, l, m, r) is a key process that assumes that arr[l..m] and arr[m+1..r] are sorted
and merges the two sorted sub-arrays into one.
Time Complexity: O(n log n) in all cases (worst, average and best)
    Space Complexity: O(n) auxiliary space
.'''

#first we will start from the basic understanding that how we can merge two sorted arrays
def merge_sorted(left,right):
    fin_arr = []
    i =j=0
    n=len(left)
    m=len(right)
    while i<n and j<m:
        if left[i]<right[j]:
            fin_arr.append(left[i])
            i+=1
        else:
            fin_arr.append(right[j])
            j+=1
    # these conditions are to check if any element is left in either of the arrays beacuse there wont be 
    # equal elements in both the arrays everytime
    if i<n:
        while i<n:
            fin_arr.append(left[i])
            i+=1
    if j<m:
        while j<m:
            fin_arr.append(right[j])
            j+=1
            
    return fin_arr

'''Now lets study how to divide an array into two halves recursively and then merge them using the above function'''
def merge_sort(arr):
    # Since this will invole recursion we need a base case to stop the infite recursion
    if len(arr)<=1:
        return arr     # means if the array has one or no element we return the array as it is already sorted
    mid = len(arr)//2  # finding the mid index to divide the array into two halves
    left_half = arr[:mid]  # slcing the array from start to mid index and calling merge_sort recursively
    right_half = arr[mid:]  # slicing the array from mid index to end and calling merge_sort recursively
    left_sorted = merge_sort(left_half)  # recursive call to sort the left half
    right_sorted = merge_sort(right_half)  # recursive call to sort the right half
    return merge_sorted(left_sorted,right_sorted)  # merging the two sorted halves using the merge_sorted function

nums = [38, 27, 43, 3, 9, 82, 10,50,80,8,9,7,6,5,4,5,6]
sorted_nums = merge_sort(nums)
print(sorted_nums)