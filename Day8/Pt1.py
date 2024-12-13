FILENAME = "Data.txt"
#FILENAME = "Day6\\TestData.txt"
def getFileContents(fn):
    fp = open(fn,"r")
    fc = fp.readlines()
    fp.close()
    for i in range(len(fc)):
        fc[i] = fc[i].strip()
    return fc



fc = getFileContents(FILENAME)

def formatFileContent(fc):

    results = []

    for line in fc:
        line  = line.strip()
        buffer = [x for x in line]
        results.append(buffer)

    return results

fc = formatFileContent(fc)



def findNodes(matrix):

    nodeDict = {}

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):

            if matrix[i][j] != ".":
                if matrix[i][j] not in nodeDict:
                    nodeDict.setdefault(matrix[i][j],[])
                    nodeDict[matrix[i][j]].append([i,j])
                else:
                    nodeDict[matrix[i][j]].append([i,j])
            
    return nodeDict

def isValidPos(matrix,x,y):


    if x >= 0 and y >= 0 and x < len(matrix) and y < len(matrix[0]):
        return True
    else:
        return False


def antiNodePlacer(matrix,points,blankMatrix):



    #matrixPrint(newMatrix)
    
    for j in range(len(points)):
        currentPoint = points[j]

        for i in range(1,len(points)):
            if i != j and i > j:
                diffX = abs(currentPoint[0] - points[i][0])
                diffY = currentPoint[1] - points[i][1]

                if diffY < 0:
                    diffY = abs(diffY)
                    if isValidPos(matrix,currentPoint[0]-diffX,currentPoint[1]-diffY):
                        #if matrix[currentPoint[0]-diffX][currentPoint[1]-diffY] == ".":
                        blankMatrix[currentPoint[0]-diffX][currentPoint[1]-diffY] = "#"
                    
                    if isValidPos(matrix,points[i][0]+diffX,points[i][1]+diffY):
                        #if matrix[points[i][0]+diffX][points[i][1]+diffY] == ".":
                        blankMatrix[points[i][0]+diffX][points[i][1]+diffY] = "#"
                elif diffY > 0:

                    if isValidPos(matrix,currentPoint[0]-diffX,currentPoint[1]+diffY):
                        #if matrix[currentPoint[0]-diffX][currentPoint[1]+diffY] == ".":
                        blankMatrix[currentPoint[0]-diffX][currentPoint[1]+diffY] = "#"
                    if isValidPos(matrix,points[i][0]+diffX,points[i][1]-diffY):
                        #if matrix[points[i][0]+diffX][points[i][1]-diffY] == ".":
                        blankMatrix[points[i][0]+diffX][points[i][1]-diffY] = "#"


def matrixPrint(matrix):


    for line in matrix:
        for val in line:
            print(val,end="")
        print()
    print()

def findAllMarks(matrix):

    total = 0

    for line in matrix:
        for val in line:
            if val == "#":
                total += 1
    return total

allNodes = findNodes(fc)
#print("ALL NODES")
#print(allNodes)
#print("")

#matrixPrint(fc)
print()

blankMatrix = []


for line in fc:
    buffer = []
    for val in line:
        buffer.append(".")
    blankMatrix.append(buffer)

matrixPrint(blankMatrix)

for key in allNodes:

    antiNodePlacer(fc,allNodes[key],blankMatrix)

matrixPrint(blankMatrix)


print("Total antinodes: " + str(findAllMarks(blankMatrix)))



