
'''Problem: Write a function multiply_list(numbers, factor) that takes a list of numbers and a single factor (an integer). The function should return a new list where every element from the original list is multiplied by the factor.

Example: multiply_list([1, 2, 3], 10) should return [10, 20, 30].


def multiply_list(numbers, factor):
    newlisit =[]
    for n in numbers:
        newlisit.append(n*factor)
    return newlisit
print (multiply_list([10,20,30],5)) '''


'''2. Count Occurrences
Problem: Write a function count_item(data_list, target) that takes a list and a target item. Use a for loop to count how many times the target appears in the data_list and return the count.

Example: count_item(['apple', 'banana', 'apple', 'orange'], 'apple') should return'''

'''def count_item(data_list, target):
    count =0
    for items in data_list :
        if items == target:
            count=count+1

    return count 
print(count_item(['asad','shafi','zainab','abeeha','asad','shafi','asad'],'shafi'))'''

'''3. Filter Vowels
Problem: Write a function get_vowels(word) that takes a string. Use a loop to iterate through the characters and return a list containing only the vowels (a, e, i, o, u).

Example: get_vowels("hello") should return ['e', 'o'].'''
'''def get_vowels(word):
    vowels ='aeiou'
    vowelslist =[]
    for char in word.lower():
        if char in vowels:
            vowelslist.append(char)
    return vowelslist
print(get_vowels('lgorithms my name is khan and i a am not a terrorist'))'''

'''def unique_elements(input_list):
    newlist=[]
    for i in input_list:
        if i not in newlist:
            newlist.append(i)
    return newlist 
print(unique_elements([10,20,30,20,30,40,50,50,60,65]))'''

'''def reverse_manual(input_list):
    rev_list=[]
    for i in range(len(input_list)-1,-1,-1):
        rev_list.append(input_list[i])
    return rev_list
print (reverse_manual([1,2,3,4,5,6,7,8,'shafi']))'''

def find_common(list1, list2):
    coomon =[]
    for i in list1:
        if i in list2 and i not in coomon:
            coomon.append(i)
    return coomon
print(find_common([1,2,3,4,5,6],[2,8,7,5,4,3]))
