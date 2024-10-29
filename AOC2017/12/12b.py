file = 'test.txt'
file = 'input.txt'

with open(file) as inp:
    z = inp.read()
    z = z.strip()

nodes = {}
for line in z.split('\n'):
    l,r = line.split(' <-> ')
    l = int(l)
    nodes[l] = set()
    for x in r.split(', '):
        n = int(x)
        nodes[l].add(n)

seen = set()

groups = 0
for n in range(len(nodes)):
    if n not in seen:
        groups += 1
        seen.add(n)
        toExpand = {n}
        while len(toExpand) > 0:
            n = toExpand.pop()
            for node in nodes[n]:
                if node not in seen:
                    seen.add(node)
                    toExpand.add(node)

print(groups)