nums=[-2,1,-3,1,4,-4,-3]
n=len(nums)
maxi=float('-inf')
for i in range(0,n):
    total=0
    for j in range(i,n):
        total+=nums[j]
        maxi=max(maxi,total)
print("Maximum subarray sum is:",maxi)
#now using kadane's algorithm
max_ending_here=0
max_so_far=float('-inf')

for i in range(n):
    max_ending_here += nums[i]
    if max_so_far < max_ending_here:
        max_so_far = max_ending_here
    if max_ending_here < 0:
        max_ending_here = 0

print("Maximum subarray sum using Kadane's algorithm is:", max_so_far)