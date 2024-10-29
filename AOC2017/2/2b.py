file,parse = 'test.txt',' '
file,parse = 'input.txt','\t'

with open(file) as inp:
    z = inp.read()
    z = z.strip()

ans = 0

for line in z.split('\n'):
    numbers = []
    for s in line.split(parse):
        if len(s) == 0:
            continue
        numbers.append(int(s))
    for i in range(0,len(numbers)):
        for j in range(i+1,len(numbers)):
            smallest = min(numbers[i],numbers[j])
            biggest = max(numbers[i],numbers[j])
            if biggest % smallest == 0:
                ans += biggest // smallest

print(ans)