file = 'test.txt'
file = 'input.txt'

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

i = 0
while 0 <= i and i < len(commands):
    cmd,X,Y = commands[i].split(' ')
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
            ans += 1
        case 'jnz':
            if type(X) is type(17) or registers[X] != 0:
                i += Y - 1
        case _:
            print(f'error: cmd was {cmd}')
    i += 1

print(registers)
print(ans)