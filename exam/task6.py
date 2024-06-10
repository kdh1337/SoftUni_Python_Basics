number = int(input())
number_str = str(number)

for digit1 in range(1, int(number_str[2]) + 1):
    for digit2 in range(1, int(number_str[1]) + 1):
        for digit3 in range(1, int(number_str[0]) + 1):

            result = digit1 * digit2 * digit3
            print(f'{digit1} * {digit2} * {digit3} = {result};')