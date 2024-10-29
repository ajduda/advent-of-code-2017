file = 'test.txt'
file = 'input.txt'

MAX = 256

APPEND = [17, 31, 73, 47, 23]

with open(file) as inp:
    z = inp.read()
    z = z.strip()

numbers = list(range(MAX))
sequence = []

for line in z.split('\n'):
    for c in line:
        sequence.append(ord(c))

for n in APPEND:
    sequence.append(n)


skip = 0
pos = 0

for _ in range(64):
    for n in sequence:
        if n + pos >= MAX:
            l1 = numbers[pos:]
            l2 = numbers[:(n+pos)%MAX]
            for x in l2:
                l1.append(x)
            l1.reverse()
            for i in range(len(l1)):
                numbers[(pos+i)%MAX] = l1[i]
        else:
            l = numbers[pos:pos+n]
            l.reverse()
            for i in range(len(l)):
                numbers[pos+i] = l[i]
        pos += n
        pos += skip
        pos %= MAX
        skip += 1

s = ''
for block in range(16):
    i = block*16
    xor = 0
    for n in range(i,i+16):
        xor ^= numbers[n]
    s += hex(xor)[2:]
print(s)