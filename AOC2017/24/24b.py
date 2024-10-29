def findBest(pieces,lookup,used,portVal,length):
    best = 0
    bestLength = length
    for idx in lookup[portVal]-used:
        l,r = pieces[idx]
        if l == portVal:
            nextPortVal = r
        else:
            nextPortVal = l
        tempLen,tempBest = findBest(pieces,lookup,used|{idx},nextPortVal,length+1)
        tempBest += l + r
        if tempLen > bestLength:
            bestLength = tempLen
            best = tempBest
        elif tempLen == bestLength:
            if tempBest > best:
                best = tempBest
    return (bestLength,best)

file = 'test.txt'
file = 'input.txt'

with open(file) as inp:
    z = inp.read()
    z = z.strip()

ans = 0

i = 0
pieces = []
lookup = {}
for line in z.split('\n'):
    l,r = line.split('/')
    l = int(l)
    r = int(r)
    pieces.append((l,r))
    if l in lookup:
        lookup[l].add(i)
    else:
        lookup[l] = {i}
    if r in lookup:
        lookup[r].add(i)
    else:
        lookup[r] = {i}
    i += 1

#print(pieces)
#print(lookup)
#best = 0
#for k in lookup:
#    print(k)
#    ret = findBest(pieces,lookup,set(),k)
#    if r > best:
#        best = ret

best = findBest(pieces,lookup,set(),0,0)

print(best)