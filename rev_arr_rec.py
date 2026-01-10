num = [5, 7, 3, 2, 6, 1, 5, 9]

def rev_arr(arr, left, right):
    """Recursively reverse array in-place"""
    if left >= right:
        return
    arr[left], arr[right] = arr[right], arr[left]
    rev_arr(arr, left + 1, right - 1)

# Call the function
print("Original array:", num)
rev_arr(num, 0, 5)
print("Reversed array:", num)
    
    
