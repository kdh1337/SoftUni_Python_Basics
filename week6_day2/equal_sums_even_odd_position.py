number1 = int(input())
number2 = int(input())

for i in range(number1, number2 + 1):
    number_string = str(i)
    even_sum = 0
    odd_sum = 0
    is_even = 1

    for digit in number_string:
        if is_even % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)

        is_even += 1

    if even_sum == odd_sum:
        print(i, end=" ")