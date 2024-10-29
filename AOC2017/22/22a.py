file = 'test.txt'
file = 'input.txt'

ITERATIONS = 10000

dirs = [(-1,0),(0,1),(1,0),(0,-1)]

with open(file) as inp:
    z = inp.read()
    z = z.strip()

ans = 0

virus = set()

y = 0
for line in z.split('\n'):
    x = 0
    for c in line:
        if c == '#':
            virus.add((y,x))
        x += 1
    y += 1

start = (y//2,x//2)
d = 0  # starts facing up
y,x = start
for i in range(ITERATIONS):
    if (y,x) in virus:
        virus.remove((y,x))
        d += 1
        d %= 4
    else:
        virus.add((y,x))
        d -= 1
        d %= 4
        ans += 1
    dy,dx = dirs[d]
    y += dy
    x += dx
print(ans)