file = 'test.txt'
file = 'input.txt'

with open(file) as inp:
    z = inp.read()
    z = z.strip()

ans = 0

scanners = []  # scanner x positions
depths = []  # each scanners y position
maxDepth = [] # the furthest down each scanner can go
directions = [] # is the scanner going up or down? True is down, False is up

for line in z.split('\n'):
    a,b = line.split(': ')
    scanners.append(int(a))
    maxDepth.append(int(b))
    depths.append(1)
    directions.append(True)

packet = -1

for _ in range(scanners[-1]+1):
    packet += 1
    if packet in scanners:
        i = scanners.index(packet)
        if depths[i] == 1:
            ans += (packet * maxDepth[i])
    for i in range(0,len(scanners)):
        if directions[i]:
            depths[i] += 1
            if depths[i] == maxDepth[i]:
                directions[i] = False
        else:
            depths[i] -= 1
            if depths[i] == 1:
                directions[i] = True


print(ans)