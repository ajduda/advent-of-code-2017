file = 'test.txt'
file = 'input.txt'

with open(file) as inp:
    z = inp.read()
    z = z.strip()

instructions = []

for line in z.split('\n'):
    instructions.append(int(line))

ans = 0
ptr = 0
while ptr >= 0 and ptr < len(instructions):
    val = instructions[ptr]
    if val >= 3:
        instructions[ptr] -= 1
    else:
        instructions[ptr] += 1
    ptr += val
    ans += 1

print(ans)