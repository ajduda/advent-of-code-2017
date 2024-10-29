file = 'test.txt'
file = 'input.txt'

def dist(y,x):
    steps = 0
    while x > 0:
        x -= 1
        if y > 0:
            y -= 1
        else:
            y += 1
        steps += 1
    while x < 0:
        x += 1
        if y > 0:
            y -= 1
        else:
            y += 1
        steps += 1
    while y > 0:
        y -= 2
        steps += 1
    while y < 0:
        y += 2
        steps += 1
    return steps

with open(file) as inp:
    z = inp.read()
    z = z.strip()

for line in z.split('\n'):
    y = 0
    x = 0
    biggest = 0
    for d in line.split(','):
        match d:
            case 'n':
                y += 2
            case 'ne':
                y += 1
                x += 1
            case 'nw':
                y += 1
                x -= 1
            case 'sw':
                y -= 1
                x -= 1
            case 'se':
                y -= 1
                x += 1
            case 's':
                y -= 2
            case _:
                print(f'ERROR: Direction was {d}')
                exit()
        myDist = dist(y,x)
        if myDist > biggest:
            biggest = myDist

    print(biggest)

