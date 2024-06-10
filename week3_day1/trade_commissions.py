city = input()
sales = float(input())
commission = 0

valid_city = city == 'Sofia' or city == 'Varna' or city == 'Plovdiv'
valid_sales = sales > 0

if not valid_city:
    print('error')
elif not valid_sales:
    print('error')

elif city == 'Sofia':
    if sales <= 500:
        commission = 0.05
    if sales > 500 and sales <= 1000:
        commission = 0.07
    if sales > 1000 and sales <= 10000:
        commission = 0.08
    if sales > 10000:
        commission = 0.12
    print(f'{commission * sales:.2f}')

elif city == 'Varna':
    if sales <= 500:
        commission = 0.045
    if sales > 500 and sales <= 1000:
        commission = 0.075
    if sales > 1000 and sales <= 10000:
        commission = 0.10
    if sales > 10000:
        commission = 0.13
    print(f'{commission * sales:.2f}')

elif city == 'Plovdiv':
    if sales <= 500:
        commission = 0.055
    if sales > 500 and sales <= 1000:
        commission = 0.08
    if sales > 1000 and sales <= 10000:
        commission = 0.12
    if sales > 10000:
        commission = 0.145
    print(f'{commission * sales:.2f}')