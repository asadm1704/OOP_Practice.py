#brtitle Search Insert Position

nums = [1,2,3,4,5,6,7,8,9,10,11,12,15,18,20]
target = 13

def search_insert_position(nums, target):
    # Find the insertion position
    for i in range(len(nums)):
        if nums[i]==target:
            return i, nums  # Return index and original list (no insertion needed)
        elif nums[i] > target:  # Found position to insert
            return i, nums[:i] + [target] + nums[i:]
    # If target is larger than all elements
    return len(nums), nums + [target]

# Get result
index, new_list = search_insert_position(nums, target)

print(f"Original list: {nums}")
print(f"Target: {target}")
print(f"Insertion index: {index}")
print(f"New list: {new_list}")
print(f"Element at index {index} in new list: {new_list[index]}")


#by binary search approach
def search_insert_position_binary_search(nums, target):
    low = 0
    high = len(nums) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid, nums  # Target found
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    # At the end of loop, low is the insertion point
    return low, nums[:low] + [target] + nums[low:]