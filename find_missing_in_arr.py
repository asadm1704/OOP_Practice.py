nums=[1,4,3,5,7,9,7,6,0]
n=len(nums)
for i in range (0,n+1):
    if i not in nums:
        print(i)
        
        break
    else:
        print("All numbers are present")    


#another alternative solution is by using dictionary
num_dict={}
for i in range(0,n+1):
    num_dict[i]=0  # filling dictonary with keys from 0 to n and initial value 0
for num in nums:
    num_dict[num]=1  # marking the presence of number in the dictionary
for key in num_dict:
    if num_dict[key]==0:
        print(key)
        break
    