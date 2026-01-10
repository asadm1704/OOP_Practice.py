n = 12321
original = n
result = 0
while n > 0:
    lastdig = n % 10
    result = (result * 10) + lastdig
    n //= 10

if original == result:
    print('Yes, the number is a palindrome')
else:
    print('No, the number is not a palindrome')