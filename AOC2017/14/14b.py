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
        b = bin(xor)[2:]
        while len(b) < 8:
            b = '0' + b
        s += b
    return s

file = 'test.txt'
file = 'input.txt'

with open(file) as inp:
    z = inp.read()
    z = z.strip()

ans = 0

for line in z.split('\n'):
    base = line
    base += '-'

strs = []

for i in range(128):
    s = base + str(i)
    h = knot_hash(s)
    strs.append(h)

visited = set()

for y in range(len(strs)):
    for x in range(len(strs[y])):
        if strs[y][x] == '1' and (y,x) not in visited:
            ans += 1
            visited.add((y,x))
            toExpand = {(y,x)}
            while len(toExpand) > 0:
                (a,b) = toExpand.pop()
                if a > 0 and strs[a-1][b] == '1' and (a-1,b) not in visited:
                    visited.add((a-1,b))
                    toExpand.add((a-1,b))
                if a < 127 and strs[a+1][b] == '1' and (a+1,b) not in visited:
                    visited.add((a+1,b))
                    toExpand.add((a+1,b))
                if b > 0 and strs[a][b-1] == '1' and (a,b-1) not in visited:
                    visited.add((a,b-1))
                    toExpand.add((a,b-1))
                if b < 127 and strs[a][b+1] == '1' and (a,b+1) not in visited:
                    visited.add((a,b+1))
                    toExpand.add((a,b+1))                

print(ans)