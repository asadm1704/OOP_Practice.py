from math import log10

num = int(input("Enter a number to make it reverse: "))
original = num
count = 0
while num > 0:
    count += 1
    lastdig = num % 10
    print(lastdig)
    num //= 10
print("Total digits are:", count)

def count_digits(n: int) -> int:
    n = abs(n)
    if n == 0:
        return 1
    return int(log10(n)) + 1

print(count_digits(original))