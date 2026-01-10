'''for a given string s and a list of characters q,
   the code counts the frequency of each character in s
   and then prints the frequency of each character in q in lowercase'''
s='abscsessassAQDEasdssadaa'
q=['a','s','d','e','c', 'b','A']
hash_list=[]
hash_list= [0] * 127
for i in s:
  ascii_value= ord(i)
  index = ascii_value - 127
  hash_list[index] +=1
for j in q:
  ascii_value_q= ord(j)
  index_q= ascii_value_q -127
  print(hash_list[index_q])
  