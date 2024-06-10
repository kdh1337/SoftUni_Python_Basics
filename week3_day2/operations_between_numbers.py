number1 = int(input())
number2 = int(input())
action = input()

if action == '+':
    result = number1 + number2
    if result % 2 == 0:
        even_odd = 'even'
    else:
        even_odd = 'odd'
    print(f'{number1} {action} {number2} = {result} - {even_odd}')

elif action == '-':
    result = number1 - number2
    if result % 2 == 0:
        even_odd = 'even'
    else:
        even_odd = 'odd'
    print(f'{number1} {action} {number2} = {result} - {even_odd}')

elif action == '*':
    result = number1 * number2
    if result % 2 == 0:
        even_odd = 'even'
    else:
        even_odd = 'odd'
    print(f'{number1} {action} {number2} = {result} - {even_odd}')

elif action == '/' and number2 != 0:
    result = number1 / number2
    print(f'{number1} / {number2} = {result:.2f}')

elif action == '%' and number2 != 0:
    result = number1 % number2
    print(f'{number1} % {number2} = {result}')

elif action == '/' or action == '%' and number2 == 0:
    print(f'Cannot divide {number1} by zero')