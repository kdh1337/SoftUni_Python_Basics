actor_name = input()
academy_points = float(input())
number_judges = int(input())
judge_points = 0

for i in range(1, number_judges + 1):
    judge_name = input()
    judge_points += (len(judge_name) * float(input())) / 2
    total_points = academy_points + judge_points
    if total_points > 1250.5:
        print(f'Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!')
        break

if total_points < 1250.5:
    print(f'Sorry, {actor_name} you need {1250.5 - total_points:.1f} more!')