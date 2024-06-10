destination = input()
min_budget = float(input())
budget = 0

while destination != 'End':
    save = int(input())
    budget += save
    if budget >= min_budget:
        print(f'Going to {destination}!')
        destination = input()
        if destination == 'End':
            break
        min_budget = float(input())
        budget = 0