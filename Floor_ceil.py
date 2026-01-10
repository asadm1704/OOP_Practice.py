#optimal solution
target = 10
nums=[1,2,3,4,5,6,7,8,9,11,12,13,14,15]
floor=-1
ceiling=-1
low=0
high=len(nums)-1
while low<=high:
    mid=(low +high)//2
    if nums [mid]==target:
        floor=nums[mid]
        ceiling=nums[mid]
        break
    elif nums[mid]>target:
        ceiling=nums[mid]
        high=mid -1
    else:
        floor=nums[mid]
        low=mid +1
print(f"floor of {target} is {floor}")
print(f"ceiling of {target} is {ceiling}")
