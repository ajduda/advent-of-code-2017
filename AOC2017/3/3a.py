n = 14
n = 347991

i = 1
while i*i < n:
    i += 1
i -= 1

print(f'sqrt rounds down to {i}')
# both test and input are odd sqrt's
base = i*i
print(n - (i*i))
y = (i // 2)
yLower = y * -1
x = y
x += 1
base += 1

while y >= yLower and base < n:
    y -= 1
    base += 1

while base < n:
    x -= 1
    base += 1
print((x,y))
print(abs(x)+abs(y))