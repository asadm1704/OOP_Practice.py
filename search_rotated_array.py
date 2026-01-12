'''Search in Rotated Sorted Array
Given a rotated sorted array, find the target value and return its index.
If target not found, return -1.
Example: nums = [17, 18, 20, 1, 3, 4, 5, 7, 8, 10, 11, 13, 14, 16], target = 5
Expected: index = 6
'''

def searchRotatedArray(nums, target):
    """
    Search for target in rotated sorted array using binary search.
    
    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    low = 0
    high = len(nums) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        # If target found at mid
        if nums[mid] == target:
            return mid
        
        # Check if right half is sorted
        if nums[mid] <= nums[high]:
            # Right half is sorted
            if nums[mid] < target <= nums[high]:
                # Target is in right half
                low = mid + 1
            else:
                # Target is in left half
                high = mid - 1
        else:
            # Left half is sorted
            if nums[low] <= target < nums[mid]:
                # Target is in left half
                high = mid - 1
            else:
                # Target is in right half
                low = mid + 1
    
    return -1  # Target not found


# Test cases
nums = [17, 18, 20, 1, 3, 4, 5, 7, 8, 10, 11, 13, 14, 16]
target = 5

result = searchRotatedArray(nums, target)
print(f"Array: {nums}")
print(f"Target: {target}")
print(f"Index: {result}")

# Additional test cases
print("\n--- Additional Test Cases ---")
test_cases = [
    ([3, 4, 5, 1, 2], 4),
    ([4, 5, 6, 7, 0, 1, 2], 0),
    ([1], 1),
    ([3, 1], 3),
]

for arr, tgt in test_cases:
    idx = searchRotatedArray(arr, tgt)
    print(f"Array: {arr}, Target: {tgt} => Index: {idx}")