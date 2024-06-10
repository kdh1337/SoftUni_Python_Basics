start_number = input()
end_number = input()

for num1 in range(int(start_number[0]), int(end_number[0]) + 1):
    for num2 in range(int(start_number[1]), int(end_number[1]) + 1):
        for num3 in range(int(start_number[2]), int(end_number[2]) + 1):
            for num4 in range(int(start_number[3]), int(end_number[3]) + 1):
                if num1 % 2 != 0 and num2 % 2 != 0 and num3 % 2 != 0 and num4 % 2 != 0:
                    print(f'{num1}{num2}{num3}{num4}', end=' ')