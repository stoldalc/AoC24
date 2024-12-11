import os
import time
import copy
#from turtle import Turtle


FILENAME = "TestData.txt"
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
        buffer = []
        for c in line:
            buffer.append(c)
        results.append(buffer)
    return results

fc = formatFileContent(fc)

#First find the guard

#Move func

#Valid position func


def findGuard(matrix):


    for i in range(len(matrix)):

        if "^" in matrix[i]:
            return [i,matrix[i].index("^")]
    
    print("WARNING NO GUARD FOUND")


def isValidPos(matrix,x,y):
    # print("len of matrix: ",len(matrix))
    # print("X is: ",x)
    # print("len of matrix row: ",len(matrix[0]))
    # print("y is: ",y)

    if y < len(matrix[0]) and x < len(matrix) and x >= 0 and y >= 0:
        #print("Returning true")
        return True
    return False

def isSpaceEmpty(matrix,x,y):
    
    if matrix[x][y] == "#" or matrix[x][y] == "X":
        return False
    return True

def printMatrix(matrix):
    #os.system("cls")
    for row in matrix:
        for c in row:
            print(c,end="")
        print()
    print()
    #time.sleep(0.1)


def countX(matrix):
    
    total = 0

    for row in matrix:
        for c in row:
            if c == "X":
                total += 1
    return total

def rowContains(matrix,x,y,currentDir):

    if currentDir == "^":
        if "X" in col2Row(matrix,x,y)[:x] and "#" in col2Row(matrix,x,y)[:x]:
            print("Row contains true")
            return True
    elif currentDir == ">":
        if "X" in matrix[x][y:] and "#" in matrix[x][y:]:
            print("Row contains true")
            return True
    elif currentDir == "v":
        if "X" in col2Row(matrix,x,y)[x:] and "#" in col2Row(matrix,x,y)[x:]:
            print("Row contains true")
            return True
    elif currentDir == "<":
        if "X" in matrix[x][:y] and "#" in matrix[x][:y]:
            print("Row contains true")
            return True
    else:
        return False
    
def col2Row(matrix,x,y):
    
    result = []

    for i in range(len(matrix)):
        result.append(matrix[i][y])
    return result


def moveGuard(matrix):

    matrixOriginal = copy.deepcopy(matrix)
    #printMatrix(matrixOriginal)

    #Get the starting position
    currentGuardPos = findGuard(matrix)

    currentGuardDir = matrix[currentGuardPos[0]][currentGuardPos[1]]
    matrixOriginal[currentGuardPos[0]][currentGuardPos[1]] = "."
    #printMatrix(matrixOriginal)
    #print("Current guard dir: ",currentGuardDir)

    onBoard = True

    loopCount = 0

    #turt = Turtle()
    #turt.setposition(currentGuardPos[0],currentGuardPos[1])
    #turt.heading(0)

    while onBoard:

        if currentGuardDir == "^":
            if isValidPos(matrix,currentGuardPos[0]-1,currentGuardPos[1]):
                if isSpaceEmpty(matrix,currentGuardPos[0]-1,currentGuardPos[1]) and not rowContains(matrix,currentGuardPos[0],currentGuardPos[1],currentGuardDir):
                    matrix[currentGuardPos[0]][currentGuardPos[1]] = "X"
                    currentGuardPos = [currentGuardPos[0]-1,currentGuardPos[1]]
                    matrix[currentGuardPos[0]][currentGuardPos[1]] = "^"
                else:

                    if matrix[currentGuardPos[0]-1][currentGuardPos[1]] == "#":
                        currentGuardDir = ">"
                        matrix[currentGuardPos[0]][currentGuardPos[1]] = ">"
                    elif matrix[currentGuardPos[0]-1][currentGuardPos[1]] == "X" or rowContains(matrix,currentGuardPos[0],currentGuardPos[1],currentGuardDir):
                        printMatrix(matrix)
                        matrix = copy.deepcopy(matrixOriginal)
                        matrix[currentGuardPos[0]-1][currentGuardPos[1]] = "^"
                        #printMatrix(matrix)
                        loopCount += 1
            else:
                matrix[currentGuardPos[0]][currentGuardPos[1]] = "X"
                onBoard = False
        elif currentGuardDir == ">":
            if isValidPos(matrix,currentGuardPos[0],currentGuardPos[1]+1):
                if isSpaceEmpty(matrix,currentGuardPos[0],currentGuardPos[1]+1) and not rowContains(matrix,currentGuardPos[0],currentGuardPos[1],currentGuardDir):
                    matrix[currentGuardPos[0]][currentGuardPos[1]] = "X"
                    currentGuardPos = [currentGuardPos[0],currentGuardPos[1]+1]
                    matrix[currentGuardPos[0]][currentGuardPos[1]] = ">"
                else:
                    if matrix[currentGuardPos[0]][currentGuardPos[1]+1] == "#":
                        currentGuardDir = "v"
                        matrix[currentGuardPos[0]][currentGuardPos[1]] = "v"
                    elif matrix[currentGuardPos[0]][currentGuardPos[1]+1] == "X" or rowContains(matrix,currentGuardPos[0],currentGuardPos[1],currentGuardDir):
                        printMatrix(matrix)
                        matrix = copy.deepcopy(matrixOriginal)
                        matrix[currentGuardPos[0]][currentGuardPos[1]+1] = ">"
                        #printMatrix(matrix)
                        loopCount += 1
            else:
                matrix[currentGuardPos[0]][currentGuardPos[1]] = "X"
                onBoard = False
        elif currentGuardDir == "v":
            if isValidPos(matrix,currentGuardPos[0]+1,currentGuardPos[1]):
                if isSpaceEmpty(matrix,currentGuardPos[0]+1,currentGuardPos[1]) and not rowContains(matrix,currentGuardPos[0],currentGuardPos[1],currentGuardDir):
                    matrix[currentGuardPos[0]][currentGuardPos[1]] = "X"
                    currentGuardPos = [currentGuardPos[0]+1,currentGuardPos[1]]
                    matrix[currentGuardPos[0]][currentGuardPos[1]] = "v"
                else:
                    if matrix[currentGuardPos[0]+1][currentGuardPos[1]] == "#":
                        currentGuardDir = "<"
                        matrix[currentGuardPos[0]][currentGuardPos[1]] = "<"
                    elif matrix[currentGuardPos[0]+1][currentGuardPos[1]] == "X" or rowContains(matrix,currentGuardPos[0],currentGuardPos[1],currentGuardDir):
                        printMatrix(matrix)
                        matrix = copy.deepcopy(matrixOriginal)
                        matrix[currentGuardPos[0]+1][currentGuardPos[1]] = "v"
                        #printMatrix(matrix)
                        loopCount += 1
            else:
                matrix[currentGuardPos[0]][currentGuardPos[1]] = "X"
                onBoard = False
        elif currentGuardDir == "<":
            if isValidPos(matrix,currentGuardPos[0],currentGuardPos[1]-1):
                if isSpaceEmpty(matrix,currentGuardPos[0],currentGuardPos[1]-1) and not rowContains(matrix,currentGuardPos[0],currentGuardPos[1],currentGuardDir):
                    matrix[currentGuardPos[0]][currentGuardPos[1]] = "X"
                    currentGuardPos = [currentGuardPos[0],currentGuardPos[1]-1]
                    matrix[currentGuardPos[0]][currentGuardPos[1]] = "<"
                else:
                    if matrix[currentGuardPos[0]][currentGuardPos[1]-1] == "#":
                        currentGuardDir = "^"

                        matrix[currentGuardPos[0]][currentGuardPos[1]] = "^"
                    elif matrix[currentGuardPos[0]][currentGuardPos[1]-1] == "X" or rowContains(matrix,currentGuardPos[0],currentGuardPos[1],currentGuardDir):
                        printMatrix(matrix)
                        matrix = copy.deepcopy(matrixOriginal)
                        matrix[currentGuardPos[0]][currentGuardPos[1]-1] = "<"
                        #printMatrix(matrix)
                        loopCount += 1

            else:
                matrix[currentGuardPos[0]][currentGuardPos[1]] = "X"
                onBoard = False
        #printMatrix(matrix)
    print("Loop back total: ", loopCount)
    return matrix

finalMatrix = moveGuard(fc)
#printMatrix(finalMatrix)
print("Total unique spaces: ",countX(finalMatrix))
