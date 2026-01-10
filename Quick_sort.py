'''quick sort is a asorting algorithm that picks pivots in the array and place it on its correct
first of all we will create two variables low and high at the start and the end of the array
now we will acreate a pviote var and initialize it with the low of the arr
take two vars i and j and intialize it with low and high 
now iterate the i though the arr and compare each valuw with the pivot if the vlue of the 
i is greater than pivot then stop the i and run the j loop in j loop we will check the value of j
is less than pivot or not if it is less than the pivot stop the j loop and now swap the values of 
i and j once the indexes of both are overlapped true then we will swap low with the  j
'''

def partition(nums,high,low):
    pivot = nums[low]
    i=low
    j=high
    while i<j:  #here we are setting a loop to iterate i and j 
        while nums[i] <=pivot and i<=high -1:
            i+=1
        while nums[j]>pivot and j>=low+1:
            j-=1
        if i<j:
            nums[i],nums[j] = nums[j],nums[i]
    nums[low],nums[j]=nums[j],nums[low] #replacing low(pivot) with the j
    return j #returning it because from the right to j the array is already sorted so 
#next time we will only use that j recursively to iterate till the current returning adress os the j
def quicksort(nums,low,high):
    n=len(nums)
    if low <high:
        p_index=partition(nums,high,low)
        quicksort(nums,low,p_index-1)
        quicksort(nums,p_index +1,high)
        
arr = [4, 6, 2, 5, 7, 9, 1, 3]
quicksort(arr, len(arr)-1,0 )
print(arr)
