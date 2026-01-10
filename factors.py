from math import sqrt
number =int(input('please enter a number to find out its facrors :'))
factors=[]
factors2=[]
factors3=[]
for i in range (1,number+1):
    if number  % i ==0:
        factors.append(i)

print(factors)

'''now going with an effiecient way for this since the last halve of the loop doesnt give the factor except the last one so 
what i did is i stoped the loop iteration once it reached to the halve of the number and only append the last number in the last
number in the list '''

for i in range(1,int(number/2 +1)):
    if number % i ==0:
        factors2.append(i)
factors2.append(number)
print(factors2)

'''there is a more effiecient way to write ths code which will make its time complexity from O(n) to Log(n)'''
for i in range(1,int(sqrt(number))+1):
    if number % i ==0:
        factors3.append(i)
        backnumber=number // i
        factors3.append(backnumber)
        factors3.sort()
print(factors3)
    
