nums=[1,2,3,4,5,6,7,8,9,10]
target =7
def binary_search(nums,target):
    low=0
    high=len(nums)-1
    
    while low<=high:
        mid =(low +high)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]>target:
            high =mid -1
        elif nums [mid]<target:
            low = mid +1
    return -1
res=binary_search( [1,2,3,4,5,6,7,8,9],target )
print(res)   


# now by recursive approach
def binary_search_recursive(nums,target,low,high):
    if low>high :
        return -1
    
    mid =(low +high)//2
    if nums[mid]==target:
        return mid
    elif nums[mid]>target:
        return binary_search_recursive(nums,target,low,mid-1)  
    elif nums[mid]<target:
        return binary_search_recursive(nums,target,mid+1,high)

res = binary_search_recursive([1,2,3,4,5,6,7,8,9],6,0,8)
print(res)
# find smallest index such that nums[i]>=target
def find_smallest_index(nums,target):
    low=0
    high=len(nums)-1
    result=-1
    
    while low<=high:
        mid =(low +high)//2
        if nums[mid]>=target:
            result=mid
            high=mid -1
        else:
            low=mid +1
    return result
res=find_smallest_index([1,2,2,2,3,4,5,7,8,9,10],11)
print(res)
# find smallest index such that nums[i]>target
def find_strictly_greater_index(nums,target):
    low=0
    high=len(nums)-1
    result=-1
    
    while low<=high:
        mid =(low +high)//2
        if nums[mid]>target:
            result=mid
            high=mid -1
        else:
            low=mid +1
    return result
res=find_strictly_greater_index([1,2,2,2,3,4,5,7,8,9,10],5)
print(res)