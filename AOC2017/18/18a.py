file = 'test.txt'
file = 'input.txt'

with open(file) as inp:
    z = inp.read()
    z = z.strip()

registers = {}
instrs = []
sound = None

for line in z.split('\n'):
    instrs.append(line)

i = 0
while i >= 0 and i < len(instrs):
    words = instrs[i].split(' ')
    cmd = words[0]
    X = words[1]
    if X not in registers:
        registers[X] = 0
    if len(words) > 2:
        Y = words[2]
        if Y in registers:
            Y = registers[Y]
        else:
            Y = int(Y)
    match words[0]:
        case 'snd':
            sound = registers[X]
        case 'set':
            registers[X] = Y
        case 'add':
            registers[X] += Y
        case 'mul':
            registers[X] *= Y
        case 'mod':
            registers[X] %= Y
        case 'rcv':
            if registers[X] != 0:
                print(sound)
                exit()
        case 'jgz':
            if registers[X] > 0:
                i += Y - 1
        case _:
            print(f'ERROR: command was {words[0]}')
    i += 1