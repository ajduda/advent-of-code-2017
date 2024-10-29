file,MAX = 'test.txt',5
file,MAX = 'input.txt',256

with open(file) as inp:
    z = inp.read()
    z = z.strip()

numbers = list(range(MAX))

skip = 0
pos = 0
for line in z.split('\n'):
    for s in line.split(','):
        n = int(s)
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
print(numbers[0]*numbers[1])

