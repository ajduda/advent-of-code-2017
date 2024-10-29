file = 'test.txt'
file = 'input.txt'

with open(file) as inp:
    z = inp.read()
    z = z.strip()

ans = 0

diff = len(z) // 2

for i in range(0,diff):
    if i + diff < len(z):
        if z[i] == z[i+diff]:
            ans += int(z[i]) * 2
print(ans)