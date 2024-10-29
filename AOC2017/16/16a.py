file,SIZE = 'test.txt',5
file,SIZE = 'input.txt',16

arr = list()

n = ord('a')

for i in range(SIZE):
    arr.append(chr(n+i))

with open(file) as inp:
    z = inp.read()
    z = z.strip()

for move in z.split(','):
    c = move[0]
    s = move[1:]
    #print(arr)
    match c:
        case 's':
            n = int(s)
            arr = arr[-1*n:] + arr[:-1*n]
        case 'x':
            a,b = s.split('/')
            a = int(a)
            b = int(b)
            temp = arr[a]
            arr[a] = arr[b]
            arr[b] = temp
        case 'p':
            a,b = s.split('/')
            i1 = arr.index(a)
            i2 = arr.index(b)
            arr[i1] = b
            arr[i2] = a
        case _:
            print(f'ERROR: case was {c};')
            exit()

s = ''
for c in arr:
    s += c
print(s)