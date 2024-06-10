width = int(input())
length = int(input())
height = int(input())
space = width * length * height
boxes = input()
total_boxes = 0

while boxes != 'Done':
    boxes = int(boxes)
    total_boxes += boxes
    if space < total_boxes:
        print(f'No more free space! You need {total_boxes - space} Cubic meters more.')
        break
    boxes = input()

if boxes == 'Done':
    print(f'{space - total_boxes} Cubic meters left.')