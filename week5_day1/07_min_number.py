import sys

number = input()
min_number = sys.maxsize

while number != 'Stop':
    n = int(number)
    if min_number > n:
        min_number = n
    number = input()

print(min_number)