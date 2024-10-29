file = 'test.txt'
file = 'input.txt'

#I stole this from myself, which I stole from the internet. I used to know how to prove this.
def lcm(a, b):
    t = a % b
    if t == 0: return a
    return a * lcm(b, t) // t


with open(file) as inp:
    z = inp.read()
    z = z.strip()

scanners = []  # scanner x positions
period = []

for line in z.split('\n'):
    a,b = line.split(': ')
    a = int(a)
    b = int(b)
    scanners.append(a)
    period.append((b*2)-2)

allPeriods = set(period)

LCM = 1
for p in allPeriods:
    LCM = lcm(LCM,p)

valid = list()
print(f'Creating a list of {LCM} True values')
for i in range(0,LCM):
    valid.append(True)

for i in range(len(scanners)):
    print(f'Beginning scanner at line {scanners[i]}')
    p = period[i]
    n = (scanners[i] * -1) % p
    while n < len(valid):
        valid[n] = False
        n += p

i = 0
while not valid[i]:
    i += 1
print(i)
