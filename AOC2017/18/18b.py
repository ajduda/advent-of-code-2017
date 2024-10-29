file = 'test.txt'
file = 'input.txt'

with open(file) as inp:
    z = inp.read()
    z = z.strip()

registers1 = {}
registers1['p'] = 0
registers1['1'] = 1
registers2 = {}
registers2['p'] = 1
registers2['1'] = 1
instrs = []
ans = 0


for line in z.split('\n'):
    instrs.append(line)

i1 = 0
i2 = 0
running1 = True
running2 = True
sendingTo2 = []
sendingTo1 = []

while running1 or running2:
    registers = registers1
    while running1:
        if i1 < 0 or i1 >= len(instrs):
            running1 = False
            break
        words = instrs[i1].split(' ')
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
                sendingTo2.append(registers[X])
                running2 = True
            case 'set':
                registers[X] = Y
            case 'add':
                registers[X] += Y
            case 'mul':
                registers[X] *= Y
            case 'mod':
                registers[X] %= Y
            case 'rcv':
                if len(sendingTo1) == 0:
                    running1 = False
                    break
                else:
                    registers[X] = sendingTo1.pop(0)
            case 'jgz':
                if registers[X] > 0:
                    i1 += Y - 1
            case _:
                print(f'ERROR: command was {words[0]}')
        i1 += 1

    registers = registers2
    while running2:
        if i2 < 0 or i2 >= len(instrs):
            running2 = False
            break
        words = instrs[i2].split(' ')
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
                sendingTo1.append(registers[X])
                running1 = True
                ans += 1
            case 'set':
                registers[X] = Y
            case 'add':
                registers[X] += Y
            case 'mul':
                registers[X] *= Y
            case 'mod':
                registers[X] %= Y
            case 'rcv':
                if len(sendingTo2) == 0:
                    running2 = False
                    break
                else:
                    registers[X] = sendingTo2.pop(0)
            case 'jgz':
                if registers[X] > 0:
                    i2 += Y - 1
            case _:
                print(f'ERROR: command was {words[0]}')
        i2 += 1

print(ans)