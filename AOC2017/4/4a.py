file = 'test.txt'
file = 'input.txt'

with open(file) as inp:
    z = inp.read()
    z = z.strip()

ans = 0

for line in z.split('\n'):
    words = set()
    for word in line.split(' '):
        if word in words:
            ans -= 1
            break
        words.add(word)
    ans += 1

print(ans)