'''given_list=[1,2,3,4,1,2,4,3,5,2,3,4,5,1,2,3,1]
empty_dic={}
for i in range(0,len(given_list)):
    if given_list[i] not in empty_dic:
        empty_dic[given_list[i]]=1
    elif given_list[i] in empty_dic:
       empty_dic[given_list[i]]+=1
print(empty_dic)


given_list2=[1,2,3,4,1,2,4,3,5,2,3,4,5,1,2,3,1,1,2,3,4,3,2,1,2,3,4,5,3,2,1,3]
empty_dic2={}
for i in range(0,len(given_list2)):
    empty_dic2[given_list2[i]]=empty_dic2.get(given_list2[i],0)+1
print(empty_dic2)'''

'''hashing means defining pre define sets or lists to resuce time complexity'''

m =[1,2,3,4,3,2,34,5,6,7,7,9,8,6,3,2,10]
n =[1,10,11,23,5,76,4,2,4,10]
hash_list= [0] *(max(m)+1)  # allocate up to the largest value in m

for i in m:
    hash_list[i]+=1
for x in n:
    if x>10 or x<1:
        print(0)
    else:
        print(hash_list[x])
    
    