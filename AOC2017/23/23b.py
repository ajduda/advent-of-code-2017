def isPrime(n):
    if n % 2 == 0:
        return 0
    i = 3
    while i*i <= n:
        if n % i == 0:
            return 0
        i += 2
    return 1

file = 'test.txt'
file = 'input.txt'
file = 'optimiziedInput.txt'

a = 'a'
b = 'b'
c = 'c'
d = 'd'
e = 'e'
f = 'f'
g = 'g'
h = 'h'

INSPECT = [32]  # line numbers

for n in range(len(INSPECT)):
    INSPECT[n] -= 1

with open(file) as inp:
    z = inp.read()
    z = z.strip()

ans = 0

commands = []

for line in z.split('\n'):
    commands.append(line)

registers = {}
for n in range(ord('a'),ord('h')+1):
    registers[chr(n)] = 0

registers[a] = 1

print('Inspecting Start')
for i in INSPECT:
    print(f'{i}: {commands[i]}')
print('Inspecting end')

timesHit = 0
i = 0
while 0 <= i and i < len(commands):
    if i in INSPECT:
        print(f'{i}: {registers}')
    if i == 10: #set g to d*e - b, if that equals 0, f = 0. e += 1, while e != b <- Inner loop
        registers[g] = 0
        registers[f] = isPrime(registers[b])
        registers[e] = registers[b]
        registers[d] = registers[b]
        i = 24
    words = commands[i].split(' ')
    cmd = words[0]
    X = words[1]
    Y = words[2]
    if X not in registers:
        X = int(X)
    
    if Y not in registers:
        Y = int(Y)
    else:
        Y = registers[Y]
    
    match cmd:
        case 'set':
            registers[X] = Y
        case 'sub':
            registers[X] -= Y
        case 'mul':
            registers[X] *= Y
        case 'jnz':
            if type(X) is type(17) or registers[X] != 0:
                i += Y - 1
        case _:
            print(f'error: cmd was {cmd}')
    i += 1

print(registers)
print(registers['h'])
nominal = {'a': 0, 'b': 84, 'c': 84, 'd': 84, 'e': 84, 'f': 0, 'g': 0, 'h': 1}
if registers['a'] == 1:
    exit()  # nominal comparison to A's register output void when a=1
for k in nominal:
    if nominal[k] != registers[k]:
        print('ERROR')