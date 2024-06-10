country = input()
tool = input()
grade_difficulty = 0
grade_performance = 0

if country == 'Russia':
    if tool == 'ribbon':
        grade_difficulty = 9.100
        grade_performance = 9.400
    elif tool == 'hoop':
        grade_difficulty = 9.300
        grade_performance = 9.800
    elif tool == 'rope':
        grade_difficulty = 9.600
        grade_performance = 9.000

elif country == 'Bulgaria':
    if tool == 'ribbon':
        grade_difficulty = 9.600
        grade_performance = 9.400
    elif tool == 'hoop':
        grade_difficulty = 9.550
        grade_performance = 9.750
    elif tool == 'rope':
        grade_difficulty = 9.500
        grade_performance = 9.400

elif country == 'Italy':
    if tool == 'ribbon':
        grade_difficulty = 9.200
        grade_performance = 9.500
    elif tool == 'hoop':
        grade_difficulty = 9.450
        grade_performance = 9.350
    elif tool == 'rope':
        grade_difficulty = 9.700
        grade_performance = 9.150

grade = grade_difficulty + grade_performance
percent_difference = 100 - grade / 20 * 100

print(f'The team of {country} get {grade:.3f} on {tool}.')
print(f'{percent_difference:.2f}%')
