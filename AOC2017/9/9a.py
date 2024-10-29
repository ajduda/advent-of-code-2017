def score(s,i,depth):
    myScore = depth
    i += 1
    while s[i] != '}':
        if s[i] == '{':
            (subscore,i) = score(s,i,depth+1)
            myScore += subscore
        i += 1
    return (myScore,i)


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
    #print(s1)
    i = 0
    s2 = ''
    while i < len(s1):
        if s1[i] != '<':
            s2 += s1[i]
        else:
            while s1[i] != '>':
                i += 1
        i += 1
    #print(s2)
    print(score(s2,0,1)[0])