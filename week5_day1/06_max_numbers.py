import sys

number = input()
max_number = -sys.maxsize

while number != 'Stop':
    n = int(number)
    if max_number < n:
        max_number = n
    number = input()

print(max_number)