'''
weare going tomerge 2 sorted arrays into one sorted array
dublicate elements are not  allowed
'''
arr1=[1,2,3,4,5,6]
arr2=[3,4,5,6,7,8,9]

n=len(arr1)
m=len(arr2)
result=[]
i=0  
j=0
while i<n and j<m:
    if arr1[i]<=arr2[j]: #use less than or equal to to avoid dublicates
       if len(result) == 0 or result[-1]!=arr1[i]:#check for dublicates
            result.append(arr1[i])#append to result if not dublicate
       i+=1
    else:
        if len(result) == 0 or result[-1]!=arr2[j]:#check for dublicates
            result.append(arr2[j])
        j+=1
while i<n:
    if len(result) == 0 or result[-1]!=arr1[i]:
        result.append(arr1[i])
    i+=1
while j<m:
    if len(result) == 0 or result[-1]!=arr2[j]:
        result.append(arr2[j])
    j+=1
print(result)
