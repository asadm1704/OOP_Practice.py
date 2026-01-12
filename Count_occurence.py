'''In this a sorted array will be given to us and a target 
will be given to us we have to find how many times
the target occur in the array we will solve it by both brute force
and optimal approach    '''

# brute force approach
nums = [1, 2, 2, 2, 3, 4, 5, 5, 5, 5, 6, 7]
target = 5
for i in range(len(nums)):
    if nums[i] == target:
        count = 0
        for j in range(i, len(nums)):
            if nums[j] == target:
                count += 1
        print(f"Brute Force: The target {target} occurs {count} times.")
        break

# Optimal approach using Lower Bound and Upper Bound
def lowerBound(nums, target):
    """Find first position where nums[i] >= target"""
    n = len(nums)
    lb = -1
    low = 0
    high = n - 1
    
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] >= target:
            lb = mid
            high = mid - 1
        else:
            low = mid + 1
    
    return lb

def upperBound(nums, target):
    """Find first position where nums[i] > target"""
    n = len(nums)
    ub = n
    low = 0
    high = n - 1
    
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] > target:
            ub = mid
            high = mid - 1
        else:
            low = mid + 1
    
    return ub

def searchRange(nums, target):
    """Find first and last position of target"""
    lb = lowerBound(nums, target)
    
    # If lb == -1 or element at lb is not target
    if lb == -1 or nums[lb] != target:
        return [-1, -1]
    
    ub = upperBound(nums, target)
    
    return [lb, ub - 1]

# Test the solution
result = searchRange(nums, target)
if result[0] != -1:
    count = result[1] - result[0] + 1
    print(f"Optimal (LB/UB Method): The target {target} occurs {count} times.")
    print(f"First occurrence at index: {result[0]}, Last occurrence at index: {result[1]}")
else:
    print(f"Target {target} not found in array.")