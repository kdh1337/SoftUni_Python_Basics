number = int(input())
numbers = int(input())

while number > numbers:
    numbers += int(input())

    if number <= numbers:
        break

print(numbers)