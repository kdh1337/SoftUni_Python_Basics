inpt = input()
total = 0

while inpt != 'NoMoreMoney':
    deposit = float(inpt)
    if deposit < 0:
        print('Invalid operation!')
        break
    elif deposit > 0:
        total += deposit
        print(f'Increase: {deposit:.2f}')
        inpt = input()

print(f'Total: {total:.2f}')