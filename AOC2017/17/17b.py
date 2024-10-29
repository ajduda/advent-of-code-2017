file = 'test.txt'
file = 'input.txt'

ITERATIONS = 50000000

with open(file) as inp:
    z = inp.read()
    z = z.strip()

for line in z.split('\n'):
    steps = int(line)

firstArrValue = None

idx = 0
for n in range(1,ITERATIONS+1):
    idx += steps
    idx %= n  # a convienent value the same as the length of the arr
    idx += 1
    if idx == 1:
        firstArrValue = n

print(firstArrValue)