file = 'test.txt'
file = 'input.txt'

with open(file) as inp:
    z = inp.read()
    z = z.strip()

for line in z.split('\n'):
    s1 = ''
    skip = False
    for i in range(len(line)):
        if skip:
            skip = False
            continue
        c = line[i]
        if c == '!':
            skip = True
            continue
        s1 += c
    i = 0
    s2 = ''
    ans = 0
    while i < len(s1):
        if s1[i] != '<':
            s2 += s1[i]
        else:
            while s1[i] != '>':
                i += 1
                if s1[i] != '>':
                    ans += 1
        i += 1
    print(ans)
    