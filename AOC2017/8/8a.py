file = 'test.txt'
file = 'input.txt'

with open(file) as inp:
    z = inp.read()
    z = z.strip()

ans = 0

registers = {}

#get all registers
for line in z.split('\n'):
    reg = line.split(' ')[0]
    registers[reg] = 0

for line in z.split('\n'):
    #print(registers)
    #print(line)
    words = line.split(' ')
    op = words[5]
    cond = True
    match op:
        case '>':
            cond = registers[words[4]] > int(words[6])
        case '<':
            cond = registers[words[4]] < int(words[6])
        case '==':
            cond = registers[words[4]] == int(words[6])
        case '>=':
            cond = registers[words[4]] >= int(words[6])
        case '<=':
            cond = registers[words[4]] <= int(words[6])
        case '!=':
            cond = registers[words[4]] != int(words[6])
        case _:
            print(f'error: op was {op}')
            exit()
    if cond:
        match words[1]:
            case 'inc':
                registers[words[0]] += int(words[2])
            case 'dec':
                registers[words[0]] -= int(words[2])
            case _:
                print(f'error: inc/dec was {words[1]}')
                exit()
#print(registers)

biggest = -1000000
for k in registers:
    if registers[k] > biggest:
        biggest = registers[k]




print(biggest)