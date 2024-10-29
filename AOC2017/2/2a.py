file = 'test.txt'
#file = 'input.txt'

with open(file) as inp:
    z = inp.read()
    z = z.strip()

ans = 0

for line in z.split('\n'):
    smallest = 10000000
    biggest = -10000000
    for s in line.split('\t'):
        if len(s) == 0:
            continue
        n = int(s)
        if n < smallest:
            smallest = n
        if n > biggest:
            biggest = n
    ans += biggest - smallest

print(ans)