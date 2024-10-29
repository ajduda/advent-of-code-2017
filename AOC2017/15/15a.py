file = 'test.txt'
file = 'input.txt'

AFACTOR = 16807
BFACTOR = 48271
MODULO = 2147483647
bottom16 = (2**16)-1
ITERATIONS = 40000000

with open(file) as inp:
    z = inp.read()
    z = z.strip()

ans = 0

for line in z.split('\n'):
    A,B = line.split(',')
    A = int(A)
    B = int(B)

for i in range(ITERATIONS):
    if i % 1000000 == 0:
        print(i)
    A *= AFACTOR
    B *= BFACTOR
    A %= MODULO
    B %= MODULO
    if (A & bottom16) == (B & bottom16):
        ans += 1

print(ans)