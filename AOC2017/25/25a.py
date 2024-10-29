file = 'test.txt'
file = 'input.txt'

with open(file) as inp:
    z = inp.read()
    z = z.strip()


blocks = z.split('\n\n')
state = blocks[0].split()[3][0]
position = 0
iterations = int(blocks[0].split()[-2])
blocks = blocks[1:]
setOfOn = set()

print(iterations)


states = {}
for block in blocks:
    last = []
    for line in block.split('\n'):
        last.append(line.split(' ')[-1][:-1])
    k,_,v1,lr1,s1,_,v2,lr2,s2 = last
    v1 = (v1 == '1')
    v2 = (v2 == '1')
    if lr1 == 'right':
        lr1 = 1
    else:
        lr1 = -1
    if lr2 == 'right':
        lr2 = 1
    else:
        lr2 = -1
    states[k] = [(v1,lr1,s1),(v2,lr2,s2)]

print(states)

for i in range(iterations):
    # print(f'position: {position}')
    # print(f'state: {state}')
    # print(f'on: {setOfOn}')
    currVal = 1 if position in setOfOn else 0
    write,move,nextState = states[state][currVal]
    if write:
        setOfOn.add(position)
    else:
        if position in setOfOn:
            setOfOn.remove(position)
    position += move
    state = nextState

#print(f'position: {position}')
#print(f'state: {state}')
#print(f'on: {setOfOn}')
print(len(setOfOn))