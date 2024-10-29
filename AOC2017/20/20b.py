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

escaped = 0

iteration = 0

while len(positions) > 0:
    iteration += 1
    #update coordinates
    for i in range(len(positions)):
        for j in range(3):
            velocities[i][j] += accelerations[i][j]
            positions[i][j] += velocities[i][j]

    occupied = {}
    markForDeletion = set()
    for i in range(len(positions)):
        p = positions[i]
        coord = (p[0],p[1],p[2])
        if coord not in occupied:
            occupied[coord] = [i]
        else:
            occupied[coord].append(i)
            markForDeletion.add(coord)

    idxsToRemove = []
    if len(markForDeletion) > 0:
        print('A round of deletions are starting')
    for coord in markForDeletion:
        for idx in occupied[coord]:
            idxsToRemove.append(idx)


    idxsToRemove.sort()
    idxsToRemove.reverse()  # do later idx's first so it won't affect other indexes in this calculation
    print(f'elems to remove for {coord}: {occupied[coord]} at t={iteration}')
    for i in idxsToRemove:
        print ('deleted index ',i)
        print(f'index {i} has values p={positions[i]}v={velocities[i]}a={accelerations[i]}')
        positions.pop(i)
        velocities.pop(i)
        accelerations.pop(i)

    #check to see if any remaining rocks escaped
    toRemoveSet = set()
    for d in range(0,3):
        if len(positions) == 0:
            break
        toRemove = set()
        maxA = {0}
        maxV = {0}
        maxP = {0}
        minA = {0}
        minV = {0}
        minP = {0}

        maxAVal = accelerations[0][d]
        minAVal = accelerations[0][d]
        maxVVal = velocities[0][d]
        minVVal = velocities[0][d]
        minPVal = positions[0][d]
        maxPval = positions[0][d]
        #simplifying the code writing by only tracking indexes and doing it every time. This has the opposite effect on the execution
        for i in range(1,len(positions)):
            if maxAVal == accelerations[i][d]:
                maxA.add(i)
            if minAVal == accelerations[i][d]:
                minA.add(i)
            if maxVVal == velocities[i][d]:
                maxV.add(i)
            if minVVal == velocities[i][d]:
                minV.add(i)
            if maxPval == positions[i][d]:
                maxP.add(i)
            if minPVal == positions[i][d]:
                minP.add(i)

            if maxAVal < accelerations[i][d]:
                maxA = {i}
                maxAVal = accelerations[i][d]
            if minAVal > accelerations[i][d]:
                minA = {i}
                minAVal = accelerations[i][d]
            if maxVVal < velocities[i][d]:
                maxV = {i}
                maxVVal = velocities[i][d]
            if minVVal > velocities[i][d]:
                minV = {i}
                minVVal = velocities[i][d]
            if maxPval < positions[i][d]:
                maxP = {i}
                maxPval = positions[i][d]
            if minPVal > positions[i][d]:
                minP = {i}
                minPVal = positions[i][d]


        
        #print(maxAVal,maxA)
        #print(minAVal,minA)
        #print(maxVVal,maxV)
        #print(minVVal,minV)
        #print(maxPval,maxP)
        #print(minPVal,minP)

        toRemove = maxA & maxV & maxP
        if len(toRemove) == 1:
            toRemoveSet |= toRemove
        toRemove = minA & minV & minP
        if len(toRemove) == 1:
            toRemoveSet |= toRemove

    toRemoveList = list(toRemoveSet)
    toRemoveList.sort()
    toRemoveList.reverse()
    for i in toRemoveList:
        print(f'The rock with values p={positions[i]} v={velocities[i]} a={accelerations[i]} escaped on t={iteration}')
        escaped += 1
        positions.pop(i)
        velocities.pop(i)
        accelerations.pop(i)



print('remaining lines')
for i in range(0,len(positions)):
    print(f'an escaped line: p={positions[i]} v={velocities[i]} a={accelerations[i]}')
print(len(positions))
print(escaped)