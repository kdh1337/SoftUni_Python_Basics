start_interval = int(input())
end_interval = int(input())
magic_number = int(input())

combination_counter = 0
break_condition = False

for a in range (start_interval, end_interval + 1):
    for b in range(start_interval, end_interval + 1):
        combination_counter += 1
        if a + b == magic_number:
            print(f'Combination N:{combination_counter} ({a} + {b} = {magic_number})')
            break_condition = True
            break
    if break_condition:
        break

else:
    print(f'{combination_counter} combinations - neither equals {magic_number}')