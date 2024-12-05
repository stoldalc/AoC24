FILENAME = "Day4/Data.txt"

def getFileContents(fn):

    fp = open(fn,"r")
    fc = fp.readlines()
    fp.close()
    return fc

fc = getFileContents(FILENAME)

for i in range(len(fc)):
    fc[i] = fc[i].strip()

matrixW = len(fc[i]) 
matrixH = len(fc)

emptyMatrix = []

for i in range(matrixH):

    row = []

    for j in range(matrixW):
        row.append(" ")
    emptyMatrix.append(row)

#Verify the passed in position is a valid one
def checkValidPos(x,y):

    if x < 0 or x >= matrixW or y < 0 or y >=matrixH:
        #print("Failing: X: " + str(x) + " Y: " + str(y)) 
        return False
    else:
        #print("Passing: X: " + str(x) + " Y: " + str(y)) 
        return True

def isXmas(matrix,x,y):

    if checkValidPos(x,y) and checkValidPos(x+2,y) and checkValidPos(x+1,y+1) and checkValidPos(x,y+2) and checkValidPos(x+2,y+2):
        #Check the left to right diag
        if (matrix[x][y] == "M" and matrix[x+1][y+1] == "A" and matrix[x+2][y+2] == "S") or (matrix[x][y] == "S" and matrix[x+1][y+1] == "A" and matrix[x+2][y+2] == "M"):
            #If the the left to right is either a MAS or a SM we can check the right to left diag
            if (matrix[x+2][y] == "M" and matrix[x+1][y+1] == "A" and matrix[x][y+2] == "S") or (matrix[x+2][y] == "S" and matrix[x+1][y+1] == "A" and matrix[x][y+2] == "M"):
                return True
    return False



def findXmas(fc):

    totalXmas = 0

    for i in range(matrixW):

        for j in range(matrixH):
            
            if isXmas(fc,i,j):
                totalXmas += 1
    return totalXmas

print("Total xMas found: ", findXmas(fc))