file = 'test.txt'
file = 'input.txt'

with open(file) as inp:
    z = inp.read()
    z = z.strip()

ans = 0

banks = []

for line in z.split('\n'):
    for n in line.split(' '):
        banks.append(int(n))

seen = {str(banks)}
state = None

while state not in seen:
    #print(banks)
    #print(seen)
    #I forgot this was supposed to be highest so I'm keeping the incorrect name until it's solved
    lowestIndex = 0
    lowest = banks[0]
    for i in range(1,len(banks)):
        if banks[i] > lowest:
            lowest = banks[i]
            lowestIndex = i
    increments = banks[lowestIndex]
    banks[lowestIndex] = 0
    for i in range(1,increments+1):
        banks[(lowestIndex+i)%len(banks)] += 1
    if state is not None:
        seen.add(state)
    state = str(banks)


print(len(seen))