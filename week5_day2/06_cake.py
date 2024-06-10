length = int(input())
width = int(input())
pieces = input()
size = length * width

while pieces != 'STOP':
    pieces = int(pieces)
    if size < pieces:
        print(f'No more cake left! You need {pieces - size} pieces more.')
        break
    size -= pieces
    pieces = input()

if pieces == 'STOP':
    print(f'{size} pieces are left.')