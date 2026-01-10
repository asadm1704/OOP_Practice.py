'''when  a function calls itself directly or indirectly is called recursion.
   it is used to solve problems that can be broken down into smaller, repetitive sub-problems.'''
'''asad = 0

def recursion_func():
    global asad
    if asad == 4:
        return
    print('asad')
    asad += 1
    recursion_func() 

recursion_func() '''

'''def function(x, n):      
    if n > 0:  # Base case - stops recursion when n reaches 0
        return
    function(x, n+1)
    print(x)    # Print the value
      # Recursive call with n decreased by 1

function('Zainab', 900)
'''
'''sum of 1 to n numbers '''
'''total = 0

def sum_of_n(n):
    global total
    if n <= 0:
        return
    total += n
    sum_of_n(n-1)
'
sum_of_n(5)'''
print(f"Sum: {total}")
# Output: Sum: 15

def fun(n):
  if n ==1:
    return 1
  return n + fun(n-1)
print(fun(5))