def knot_hash(line):

    MAX = 256
    numbers = list(range(MAX))
    sequence = []
    APPEND = [17, 31, 73, 47, 23]
    for c in line:
        sequence.append(ord(c))
    skip = 0
    pos = 0
    sequence += APPEND
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
        s += bin(xor)[2:]  # This was still hex when I ran the input
    return s

#This was how I origionally did ones when it was returning hex. I'm editing this after the fact to test my changes for b here
ones = {}
ones['0'] = 0
ones['1'] = 1
ones['2'] = 1
ones['3'] = 2
ones['4'] = 1
ones['5'] = 2
ones['6'] = 2
ones['7'] = 3
ones['8'] = 1
ones['9'] = 2
ones['a'] = 2
ones['b'] = 3
ones['c'] = 2
ones['d'] = 3
ones['e'] = 3
ones['f'] = 4

file = 'test.txt'
file = 'input.txt'

with open(file) as inp:
    z = inp.read()
    z = z.strip()

ans = 0

for line in z.split('\n'):
    base = line
    base += '-'

for i in range(128):
    s = base + str(i)
    h = knot_hash(s)
    for c in h:
        #ans += ones[c]  # The original line
        if c == '1':
            ans += 1

print(ans)