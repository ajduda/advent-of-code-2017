file = 'test.txt'
file = 'input.txt'

with open(file) as inp:
    z = inp.read()
    z = z.strip()

ans = 0

for line in z.split('\n'):
    prev = None
    for c in line:
        if c == prev:
            ans += int(c)
        prev = c
    if prev == line[0]:
        ans += int(prev)
print(ans)