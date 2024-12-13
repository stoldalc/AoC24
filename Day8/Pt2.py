import math
FILENAME = "Data.txt"
#FILENAME = "Day8\\Data.txt"
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
# for line in fc:
#     print(line)


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



def getLine(matrix,x1,y1,x2,y2):

    slope = (y2-y1)/(x2-x1)

    interc = y1 - (slope*x1)


    run = x2 - x1
    if run == 0:
        slope = 0

    if run < 0:
        run = x1-x2
    
    rise = y2-y1
    gcd_ = math.gcd(abs(rise),run)

    slope = (rise//gcd_)//(run//gcd_)




    line = [[x1,y1],[x2,y2]]


    for i in range(len(matrix)):

        y = slope * i + interc

        if y < len(matrix[0]) and y >= 0 and (y).is_integer():
            y = int(y)
            line.append([i,y])

    return line
    #y=mx+b


def antiNodePlacer(matrix,line):
    
    for point in line:
        #print(point)
        matrix[point[0]][point[1]] = "#"
    


def validAntena(ls):

    if len(ls) >= 2:
        return True
    else:
        return False



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

blankMatrix = []


for line in fc:
    buffer = []
    for val in line:
        buffer.append(".")
    blankMatrix.append(buffer)

#matrixPrint(blankMatrix)

for key in allNodes:

    if validAntena(allNodes[key]):

        values = allNodes[key]
        
        for i in range(len(values)):

            for j in range(len(values)):

                if i != j:
                    line = getLine(fc,values[i][0],values[i][1],values[j][0],values[j][1])
                    antiNodePlacer(blankMatrix,line)
                    #matrixPrint(blankMatrix)


matrixPrint(blankMatrix)


# for i in range(len(fc)):

#     for j in range(len(fc[i])):

#         if blankMatrix[i][j] == "#":
#             fc[i][j] = "#"


# for i in range(len(fc)):

#     for j in range(len(fc[i])):

#         if fc[i][j] == "#" or fc[i][j] == ".":
#             fc[i][j] = " "

matrixPrint(fc)

print("Total antinodes: " + str(findAllMarks(blankMatrix)))



