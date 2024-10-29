file = 'test.txt'
file = 'input.txt'

def findWeight(src,holding,weights):
    ret = weights[src]
    for held in holding[src]:
        ret += findWeight(held,holding,weights)
    return ret

def findWrong(root,holding,weights):
    if len(holding[root]) == 0:
        return True # We found an endpoint, disregard
    aboveWeights = []
    for held in holding[root]:
        aboveWeights.append((findWeight(held,holding,weights),held))
    print(aboveWeights)
    aboveWeights.sort()
    if aboveWeights[0][0] == aboveWeights[1][0] and aboveWeights[-1][0] == aboveWeights[-2][0]:
        return True
    if aboveWeights[0][0] != aboveWeights[1][0]:
        findWrong(aboveWeights[0][1],holding,weights)
        wrongWeight = aboveWeights[0][1]
    if aboveWeights[-1][0] != aboveWeights[-2][0]:
        findWrong(aboveWeights[-1][1],holding,weights)
        wrongWeight = aboveWeights[-1][1]
    #print(aboveWeights[1][0])  # This is the total weight, get the OG
    print(wrongWeight)
    referenceWeight = aboveWeights[1][0]
    print(referenceWeight)
    difference = referenceWeight - findWeight(wrongWeight,holding,weights)
    print(difference + weights[wrongWeight])

    exit()

with open(file) as inp:
    z = inp.read()
    z = z.strip()

holding = {}
weights = {}

for line in z.split('\n'):
    parts = line.split(' ')
    src = parts[0]
    weight = parts[1]
    weights[src] = int(weight[1:-1])  # disregard the surrounding ()'s
    holding[src] = set()
    if len(parts) > 3:
        for p in parts[3:]:
            s = p
            if s[-1] == ',':
                s = s[:-1]
            holding[src].add(s)

heldBy = {}
#initalize
for k in holding:
    heldBy[k] = set()

for k in holding:
    for v in holding[k]:
        heldBy[v].add(k)

for k in heldBy:
    if len(heldBy[k]) == 0:
        root = k
        break

findWrong(root,holding,weights)

print('this is awkward')