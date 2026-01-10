'''there are many ways to do that but the most efficient way to remove dublicate
is to convert the into the dictionary because dictionary do not allow dublicate values
then convert it back to the list'''
nums=[1,2,3,4,5,5,6,7,8,9,9,10]
n=len(nums)
freq_dict={}
for i in range(0,n):
    freq_dict[nums[i]]=0
j=0
for key in freq_dict:
    nums[j]=key
    j+=1
