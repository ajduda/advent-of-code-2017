n = 59
n = 347991

def checkDone(val,limit):
    if val > limit:
        print(val)
        exit()

def value(grid,coord):
    y,x = coord  # back to my normal y,x that grids would use
    newVal = 0
    for dx in range(-1,2):
        for dy in range(-1,2):
            if (y+dy,x+dx) in grid:
                newVal += grid[(y+dy,x+dx)]
    return newVal

grid = {}
grid[(0,0)] = 1

x = 0
y = 0
xBounds = 1
yBounds = -1
while True:
    while x < xBounds:
        x += 1
        grid[(y,x)] = value(grid,(y,x))
        checkDone(grid[(y,x)],n)
    xBounds *= -1
    while y > yBounds:
        y -= 1
        grid[(y,x)] = value(grid,(y,x))
        checkDone(grid[(y,x)],n)
    yBounds *= -1
    while x > xBounds:
        x -= 1
        grid[(y,x)] = value(grid,(y,x))
        checkDone(grid[(y,x)],n)
    xBounds *= -1
    xBounds += 1
    while y < yBounds:
        y += 1
        grid[(y,x)] = value(grid,(y,x))
        checkDone(grid[(y,x)],n)
    yBounds += 1
    yBounds *= -1