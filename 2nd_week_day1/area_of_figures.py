shape = input()
from math import pi

if shape == 'square':
    number_square = float(input())
    print(number_square * number_square)
elif shape == 'rectangle':
    number1_rectangle = float(input())
    number2_rectangle = float(input())
    print(number1_rectangle * number2_rectangle)
elif shape == 'circle':
    number_circle = float(input())
    print(pi * (number_circle * number_circle))
elif shape == 'triangle':
    number1_triangle = float(input())
    number2_triangle = float(input())
    print((number1_triangle * number2_triangle) / 2)