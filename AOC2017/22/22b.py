file = 'test.txt'
file = 'input.txt'

ITERATIONS = 10000000

dirs = [(-1,0),(0,1),(1,0),(0,-1)]

with open(file) as inp:
    z = inp.read()
    z = z.strip()

ans = 0

weakened = set()
infected = set()
flagged = set()

y = 0
for line in z.split('\n'):
    x = 0
    for c in line:
        if c == '#':
            infected.add((y,x))
        x += 1
    y += 1

start = (y//2,x//2)
d = 0  # starts facing up
y,x = start
for i in range(ITERATIONS):
    if (y,x) in weakened:
        weakened.remove((y,x))
        infected.add((y,x))
        ans += 1
        # do not turn on a weakened node
    elif (y,x) in infected:
        infected.remove((y,x))
        flagged.add((y,x))
        d += 1
        d %= 4
    elif (y,x) in flagged:
        flagged.remove((y,x))
        d += 2
        d %= 4
    else: #clean
        weakened.add((y,x))
        d -= 1
        d %= 4
    dy,dx = dirs[d]
    y += dy
    x += dx
print(ans)