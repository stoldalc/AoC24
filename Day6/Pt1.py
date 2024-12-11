import os
import time
from turtle import Turtle
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
    
    if matrix[x][y] == "#":
        return False
    return True

def printMatrix(matrix):
    os.system("cls")
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

def moveGuard(matrix):

    #Get the starting position
    currentGuardPos = findGuard(matrix)

    currentGuardDir = matrix[currentGuardPos[0]][currentGuardPos[1]]

    #print("Current guard dir: ",currentGuardDir)

    onBoard = True

    turt = Turtle()
    turt.setposition(currentGuardPos[0],currentGuardPos[1])
    #turt.heading(0)

    while onBoard:

        if currentGuardDir == "^":
            if isValidPos(matrix,currentGuardPos[0]-1,currentGuardPos[1]):
                if isSpaceEmpty(matrix,currentGuardPos[0]-1,currentGuardPos[1]):
                    matrix[currentGuardPos[0]][currentGuardPos[1]] = "X"
                    currentGuardPos = [currentGuardPos[0]-1,currentGuardPos[1]]
                    matrix[currentGuardPos[0]][currentGuardPos[1]] = "^"
                    turt.forward(10)
                else:
                    currentGuardDir = ">"
                    matrix[currentGuardPos[0]][currentGuardPos[1]] = ">"
                    turt.setheading(90)
            else:
                matrix[currentGuardPos[0]][currentGuardPos[1]] = "X"
                onBoard = False
        elif currentGuardDir == ">":
            if isValidPos(matrix,currentGuardPos[0],currentGuardPos[1]+1):
                if isSpaceEmpty(matrix,currentGuardPos[0],currentGuardPos[1]+1):
                    matrix[currentGuardPos[0]][currentGuardPos[1]] = "X"
                    currentGuardPos = [currentGuardPos[0],currentGuardPos[1]+1]
                    matrix[currentGuardPos[0]][currentGuardPos[1]] = ">"
                    turt.forward(10)
                else:
                    currentGuardDir = "v"
                    matrix[currentGuardPos[0]][currentGuardPos[1]] = "v"
                    turt.setheading(180)
            else:
                matrix[currentGuardPos[0]][currentGuardPos[1]] = "X"
                onBoard = False
        elif currentGuardDir == "v":
            if isValidPos(matrix,currentGuardPos[0]+1,currentGuardPos[1]):
                if isSpaceEmpty(matrix,currentGuardPos[0]+1,currentGuardPos[1]):
                    matrix[currentGuardPos[0]][currentGuardPos[1]] = "X"
                    currentGuardPos = [currentGuardPos[0]+1,currentGuardPos[1]]
                    matrix[currentGuardPos[0]][currentGuardPos[1]] = "v"
                    turt.forward(10)
                else:
                    currentGuardDir = "<"
                    matrix[currentGuardPos[0]][currentGuardPos[1]] = "<"
                    turt.setheading(270)
            else:
                matrix[currentGuardPos[0]][currentGuardPos[1]] = "X"
                onBoard = False
        elif currentGuardDir == "<":
            if isValidPos(matrix,currentGuardPos[0],currentGuardPos[1]-1):
                if isSpaceEmpty(matrix,currentGuardPos[0],currentGuardPos[1]-1):
                    matrix[currentGuardPos[0]][currentGuardPos[1]] = "X"
                    currentGuardPos = [currentGuardPos[0],currentGuardPos[1]-1]
                    matrix[currentGuardPos[0]][currentGuardPos[1]] = "<"
                    turt.forward(10)
                else:
                    currentGuardDir = "^"
                    matrix[currentGuardPos[0]][currentGuardPos[1]] = "^"
                    turt.setheading(0)
            else:
                matrix[currentGuardPos[0]][currentGuardPos[1]] = "X"
                onBoard = False
        #printMatrix(matrix)
    #turtle.mainloop()
    return matrix

finalMatrix = moveGuard(fc)
#printMatrix(finalMatrix)
print("Total unique spaces: ",countX(finalMatrix))
