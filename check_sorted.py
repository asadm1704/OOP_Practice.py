nums=[1,2,3,4,5,6,7,8,9,10]
for i in range(len(nums)-1):
    if nums[i]>nums[i+1]:
        print("The list is not sorted.")
        break
else:
    print("The list is sorted.")