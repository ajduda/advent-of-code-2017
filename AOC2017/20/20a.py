def magnitude(l):
    ret = 0
    for n in l:
        ret += abs(n)
    return ret

file = 'test.txt'
file = 'input.txt'

with open(file) as inp:
    z = inp.read()
    z = z.strip()

lists = []

for line in z.split('\n'):
    sections = line.split('<')
    for i in range(1,len(sections)):
        numbers = sections[i].split('>')[0]
        lists.append([])
        for n in numbers.split(','):
            lists[-1].append(int(n))


positions = []
velocities = []
accelerations = []
for i in range(len(lists)//3):
    n = i*3
    positions.append(lists[n])
    velocities.append(lists[n+1])
    accelerations.append(lists[n+2])

minimum = 100000
bestIdx = -1
for i in range(len(accelerations)):
    m = magnitude(accelerations[i])
    if m < minimum:
        minimum = m
        bestIdx = i
    if m == minimum:
        vMag1 = magnitude(velocities[i])
        vMag2 = magnitude(velocities[bestIdx])
        if vMag1 < vMag2:
            bestIdx = i
        if vMag1 == vMag2:
            pMag1 = magnitude(positions[i])
            pMag2 = magnitude(positions[bestIdx])
            if pMag1 < pMag2:
                bestIdx = i

print(bestIdx)
