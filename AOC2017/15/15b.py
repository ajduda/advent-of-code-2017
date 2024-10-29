file = 'test.txt'
file = 'input.txt'

AFACTOR = 16807
BFACTOR = 48271
MODULO = 2147483647
bottom16 = (2**16)-1
ITERATIONS = 5000000

with open(file) as inp:
    z = inp.read()
    z = z.strip()

ans = 0

for line in z.split('\n'):
    A,B = line.split(',')
    A = int(A)
    B = int(B)

for i in range(ITERATIONS):
    if i % 100000 == 0:
        print(i)
    A *= AFACTOR
    A %= MODULO
    while A % 4 != 0:
        A *= AFACTOR
        A %= MODULO
    B *= BFACTOR
    B %= MODULO
    while B % 8 != 0:
        B *= BFACTOR
        B %= MODULO
    if (A & bottom16) == (B & bottom16):
        ans += 1

print(ans)