def strToShape(s):
    shape = []
    for line in s.split('/'):
        shapeLine = []
        for c in line:
            shapeLine.append(c=='#')
        shape.append(tuple(shapeLine))
    return shape

def rotateShape(shape):
    newShape = []
    match len(shape[0]):
        case 2:
            A,B = shape[0]
            C,D = shape[1]
            newShape = [(C,A),(D,B)]
        case 3:
            A,B,C = shape[0]
            D,E,F = shape[1]
            G,H,I = shape[2]
            newShape = [(G,D,A),(H,E,B),(I,F,C)]
        case _:
            print(f'ERROR: length of side for rotate shape was {len(shape[0])}')
    return newShape

def flipShape(shape):  # vertical flip for ease
    newShape = []
    for line in shape:
        newShape.insert(0,line)
    return newShape

def insertIfNotExists(shapes,shape):
    shapeTuple = tuple(shape)
    if shapeTuple not in shapes:
        shapes.append(shapeTuple)

def addToShapes(shapeStr,shapes,rotationsAndFlips):
    shape = strToShape(shapeStr)
    insertIfNotExists(shapes,shape)
    if rotationsAndFlips:
        for _ in range(3):
            shape = rotateShape(shape)
            insertIfNotExists(shapes,shape)
        shape = flipShape(shape)
        insertIfNotExists(shapes,shape)
        for _ in range(3):
            shape = rotateShape(shape)
            insertIfNotExists(shapes,shape)

def getShapeIndex(shapes,shapeStr):
    if type(shapeStr) == type(''):
        shape = []
        for line in shapeStr.split('/'):
            shapeLine = []
            for c in line:
                shapeLine.append(c=='#')
            shape.append(tuple(shapeLine))
        shape = tuple(shape)
    else: #Plot twist, it wasn't a shapeStr at all, just a shape!
        shape = tuple(shapeStr)  
    return shapes.index(shape)


def printShape(shape):
    for line in shape:
        s = ''
        for val in line:
            s += '#' if val else '.'
        print(s)
    print()


#file = 'test.txt'
file = 'input.txt'

ITERATIONS = 5

with open(file) as inp:
    z = inp.read()
    z = z.strip()


shapes = []
mapping = {}

for line in z.split('\n'):
    l,r = line.split(' => ')
    addToShapes(l,shapes,True)
    addToShapes(r,shapes,False)

for line in z.split('\n'):
    l,r = line.split(' => ')
    lIdx = set()
    shape = strToShape(l)
    shapeIdx = getShapeIndex(shapes,shape)
    lIdx.add(shapeIdx)
    for _ in range(3):
        shape = rotateShape(shape)
        shapeIdx = getShapeIndex(shapes,shape)
        lIdx.add(shapeIdx)
    shape = flipShape(shape)
    shapeIdx = getShapeIndex(shapes,shape)
    lIdx.add(shapeIdx)
    for _ in range(3):
        shape = rotateShape(shape)
        shapeIdx = getShapeIndex(shapes,shape)
        lIdx.add(shapeIdx)
    
    rIdx = []
    rShape = strToShape(r)
    if len(l) == 5: # 2->3 case
        rIdx.append(getShapeIndex(shapes,rShape))
    elif len(l) == 11: # 3->4 case
        A,B,C,D = rShape[0]
        E,F,G,H = rShape[1]
        I,J,K,L = rShape[2]
        M,N,O,P = rShape[3]
        rShapes = []
        rShapes.append(((A,B),(E,F)))
        rShapes.append(((C,D),(G,H)))
        rShapes.append(((I,J),(M,N)))
        rShapes.append(((K,L),(O,P)))
        for shape in rShapes:
            rIdx.append(shapes.index(shape))
    else:
        print('we have it what I expected to be an impossible point and I am scared')
    for i in lIdx:
        mapping[i] = rIdx

#the grid will go 3 -> 4 -> 6 -> 9
#Therefore, we should make the odd case skip go 2 so it's at the next even case
ductTappedOnMapping = {}
for line in z.split('\n'):
    l,r = line.split(' => ')
    if len(l) == 5:
        continue
    #It was at this point I regret not making this specific logic it's own function
    lIdx = set()
    shape = strToShape(l)
    shapeIdx = getShapeIndex(shapes,shape)
    lIdx.add(shapeIdx)
    for _ in range(3):
        shape = rotateShape(shape)
        shapeIdx = getShapeIndex(shapes,shape)
        lIdx.add(shapeIdx)
    shape = flipShape(shape)
    shapeIdx = getShapeIndex(shapes,shape)
    lIdx.add(shapeIdx)
    for _ in range(3):
        shape = rotateShape(shape)
        shapeIdx = getShapeIndex(shapes,shape)
        lIdx.add(shapeIdx)
    intermediateShape = strToShape(r)  # 3 -> 4
    A,B,C,D = intermediateShape[0]
    E,F,G,H = intermediateShape[1]
    I,J,K,L = intermediateShape[2]
    M,N,O,P = intermediateShape[3]
    topLeft = ((A,B),(E,F))
    topRight = ((C,D),(G,H))
    bottomLeft = ((I,J),(M,N))
    bottomRight = ((K,L),(O,P))
    temp = getShapeIndex(shapes,topLeft)
    temp = mapping[temp][0]
    topLeftNewShape = shapes[temp]
    temp = getShapeIndex(shapes,topRight)
    temp = mapping[temp][0]
    topRightNewShape = shapes[temp]
    temp = getShapeIndex(shapes,bottomLeft)
    temp = mapping[temp][0]
    bottomLeftNewShape = shapes[temp]
    temp = getShapeIndex(shapes,bottomRight)
    temp = mapping[temp][0]
    bottomRightNewShape = shapes[temp]

    A1,A2,B1 = topLeftNewShape[0]
    A3,A4,B3 = topLeftNewShape[1]
    D1,D2,E1 = topLeftNewShape[2]

    B2,C1,C2 = topRightNewShape[0]
    B4,C3,C4 = topRightNewShape[1]
    E2,F1,F2 = topRightNewShape[2]

    D3,D4,E3 = bottomLeftNewShape[0]
    H1,H2,I1 = bottomLeftNewShape[1]
    H3,H4,I3 = bottomLeftNewShape[2]

    E4,F3,F4 = bottomRightNewShape[0]
    I2,J1,J2 = bottomRightNewShape[1]
    I4,J3,J4 = bottomRightNewShape[2]
    rShapes = []
    rShapes.append(((A1,A2),(A3,A4)))
    rShapes.append(((B1,B2),(B3,B4)))
    rShapes.append(((C1,C2),(C3,C4)))
    rShapes.append(((D1,D2),(D3,D4)))
    rShapes.append(((E1,E2),(E3,E4)))
    rShapes.append(((F1,F2),(F3,F4)))
    rShapes.append(((H1,H2),(H3,H4))) # It was at this moment I realized I forgot G
    rShapes.append(((I1,I2),(I3,I4)))
    rShapes.append(((J1,J2),(J3,J4)))

    rIdx = []
    for shape in rShapes:
        rIdx.append(shapes.index(shape))

    for i in lIdx:
        ductTappedOnMapping[i] = rIdx
    


startStr = ".#./..#/###"
startIdx = getShapeIndex(shapes,startStr)
shapesActive = {}
shapesActive[startIdx] = 1

cyclesLeft = ITERATIONS

odd = True
while cyclesLeft > 0:
    print(shapesActive)
    print(cyclesLeft)
    for k in shapesActive:
        print(f'Shape idx {k}, there should be {shapesActive[k]} of them')
        printShape(shapes[k])
    nextShapesActive = {}
    if odd:
        odd = False
        mapToUse = ductTappedOnMapping
        cyclesLeft -= 2
    else:
        odd = True
        mapToUse = mapping
        cyclesLeft -= 1
    
    for k in shapesActive:
        scalar = shapesActive[k]
        nextShapes = mapToUse[k]
        for shape in nextShapes:
            if shape in nextShapesActive:
                nextShapesActive[shape] += scalar
            else:
                nextShapesActive[shape] = scalar
    shapesActive = nextShapesActive


# print(shapesActive)
# for k in shapesActive:
#     print(f'Shape idx {k}, there should be {shapesActive[k]} of them')
#     printShape(shapes[k])


ans = 0
for k in shapesActive:
    onCount = 0
    active = shapesActive[k]
    for line in shapes[k]:
        for val in line:
            if val:
                onCount += 1
    ans += active * onCount

print(ans)