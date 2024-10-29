file = 'test.txt'
file = 'input.txt'

dirs = {(1,0),(-1,0),(0,1),(0,-1)}

with open(file) as inp:
    z = inp.read()
    #z = z.strip() #AHHHHHHHHHHHHHHHHHHHHHHHHHHHH

ans = 0

pluses = set()
lines = set()
letters = {}
anything = set()
pos = None
d = (1,0)

y = 0
for line in z.split('\n'):
    x = 0
    for c in line:
        if c == '+':
            pluses.add((y,x))
            anything.add((y,x))
        elif c.isalpha():
            letters[(y,x)] = c
            anything.add((y,x))
        elif c != ' ':
            lines.add((y,x))
            anything.add((y,x))
            if y == 0:
                pos = (y,x)
        x += 1
    y += 1

while pos in anything:
    y,x = pos
    dy,dx = d
    if pos not in pluses:
        y += dy
        x += dx
        ans += 1
    else:
        for nextD in dirs:
            if nextD == (d[0]*-1,d[1]*-1):
                continue
            dy2,dx2 = nextD
            if (y+dy2,x+dx2) in anything:
                d = nextD
                y += dy2
                x += dx2
                ans += 1
                break
    pos = (y,x)


print(ans)