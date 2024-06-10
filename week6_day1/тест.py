destination = input()
while destination != 'End':
    min_budget = float(input())
    budget = 0
    while True:
        save = float(input())
        budget += save
        if budget >= min_budget:
            print(f'Going to {destination}!')
            break
    destination = input()