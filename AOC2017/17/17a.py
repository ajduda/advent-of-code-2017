file = 'test.txt'
file = 'input.txt'

ITERATIONS = 2017

with open(file) as inp:
    z = inp.read()
    z = z.strip()

for line in z.split('\n'):
    steps = int(line)

arr = [0]
idx = 0
for n in range(1,ITERATIONS+1):
    idx += steps
    idx %= n  # a convienent value the same as the length of the arr
    arr.insert(idx+1,n)
    idx += 1

print(arr[idx+1])