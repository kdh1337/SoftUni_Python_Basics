deposit_amount = float(input())
deposit_deadline = int(input())
annual_interest = float(input())

accrued_interest = deposit_amount * annual_interest / 100

total_amount = deposit_amount + deposit_deadline * ((accrued_interest) / 12)

print(total_amount)