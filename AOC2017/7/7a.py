file = 'test.txt'
file = 'input.txt'

with open(file) as inp:
    z = inp.read()
    z = z.strip()

holding = {}

for line in z.split('\n'):
    parts = line.split(' ')
    src = parts[0]
    weight = parts[1]
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
        print(k)
        exit()

print('this is awkward')