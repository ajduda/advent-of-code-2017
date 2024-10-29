file = 'test.txt'
file = 'input.txt'

with open(file) as inp:
    z = inp.read()
    z = z.strip()

ans = 0

for line in z.split('\n'):
    words = set()
    for word in line.split(' '):
        wordList = list(word)
        wordList.sort()
        s = ''
        for c in wordList:
            s += c
        if s in words:
            ans -= 1
            break
        words.add(s)
    ans += 1

print(ans)