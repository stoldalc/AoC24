
FILENAME = "Day4\\Data.txt"

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
        row.append(".")
    emptyMatrix.append(row)

#Verify the passed in position is a valid one
def checkValidPos(x,y):

    if x < 0 or x >= matrixW or y < 0 or y >=matrixH:
        #print("Failing: X: " + str(x) + " Y: " + str(y)) 
        return False
    else:
        #print("Passing: X: " + str(x) + " Y: " + str(y)) 
        return True


def applyMask(matrix,path):

    for cord in path:

        emptyMatrix[cord[0]][cord[1]] = matrix[cord[0]][cord[1]]


#matrix = the file contents
# x is our current x position
# y is our current y position
# prevX is our previous x position
# prevY is our previous y position
# word is the word we are looking for
# index is the index of the letter for the word we are looking for
# Direction is the direction we are moving, as we can only move in horiz, vert, and diag, lines 
# NW N NE
# W    E
# SW S SE
def DFS(matrix, x, y, prevX, prevY, word, index, direction,path,pathCords):



    #if we are looking at a word that is greater than the length of the word
    # or if the char we are looking at is not the right charachter in the word
    # we return from this level
    #breakpoint()
    if (index > len(word)-1 or matrix[x][y] != word[index]):
        currentChar = matrix[x][y]
        return False

    #If we found the final charachter in the word
    if index == len(word)-1:
        currentChar = matrix[x][y]
        path.append(matrix[x][y])
        pathCords.append([x,y])
        applyMask(matrix,pathCords)
        #print("Word found: " + str(path))
        return True
    

    if direction == "NW":
        if checkValidPos(x-1,y-1):
            #print("NW " + str(matrix[x][y])  + " X: " + str(x) + " Y: " + str(y))                        
            path.append(matrix[x][y])
            pathCords.append([x,y])
            return DFS(matrix,x-1,y-1,x,y,word,index+1,"NW",path,pathCords)
        else:
            return False
    elif direction == "N":
        if checkValidPos(x,y-1):
            #print("N " + str(matrix[x][y])  + " X: " + str(x) + " Y: " + str(y))
            path.append(matrix[x][y])
            pathCords.append([x,y])
            return DFS(matrix,x,y-1,x,y,word,index+1,"N",path,pathCords)
        else:
            return False
    elif direction == "NE":
        if checkValidPos(x+1,y-1):
            #print("NE " + str(matrix[x][y])  + " X: " + str(x) + " Y: " + str(y))
            path.append(matrix[x][y])
            pathCords.append([x,y])
            return DFS(matrix,x+1,y-1,x,y,word,index+1,"NE",path,pathCords)
        else:
            return False
    elif direction == "E":
        if checkValidPos(x+1,y):
            #print("E " + str(matrix[x][y])  + " X: " + str(x) + " Y: " + str(y))
            path.append(matrix[x][y])
            pathCords.append([x,y])
            return DFS(matrix,x+1,y,x,y,word,index+1,"E",path,pathCords)
        else:
            return False
    elif direction == "SE":
        if checkValidPos(x+1,y+1):
            #print("SE " + str(matrix[x][y])  + " X: " + str(x) + " Y: " + str(y))
            path.append(matrix[x][y])
            pathCords.append([x,y])
            return DFS(matrix,x+1,y+1,x,y,word,index+1,"SE",path,pathCords)
        else:
            return False
    elif direction == "S":
        if checkValidPos(x,y+1):
            #print("S " + str(matrix[x][y])  + " X: " + str(x) + " Y: " + str(y))
            path.append(matrix[x][y])
            pathCords.append([x,y])
            return DFS(matrix,x,y+1,x,y,word,index+1,"S",path,pathCords)
        else:
            return False
    elif direction == "SW":
        if checkValidPos(x-1,y+1):
            #print("SW " + str(matrix[x][y])  + " X: " + str(x) + " Y: " + str(y))
            path.append(matrix[x][y])
            pathCords.append([x,y])
            return DFS(matrix,x-1,y+1,x,y,word,index+1,"SW",path,pathCords)
        else:
            return False
    elif direction == "W":
        if checkValidPos(x-1,y):
            #print("W " + str(matrix[x][y])  + " X: " + str(x) + " Y: " + str(y))
            path.append(matrix[x][y])
            pathCords.append([x,y])
            return DFS(matrix,x-1,y,x,y,word,index+1,"W",path,pathCords)
        else:
            return False


def findWord(matrix,word):

    wordTotal = 0

    for i in range(matrixW):
        #print("Outer loop: " + str(i))
        for j in range(matrixH):
            #print("Inner loop: " + str(j))
            index = 1

            if (matrix[i][j] == word[0]):

                if checkValidPos(i-1,j-1):
                    if DFS(matrix,i-1,j-1,i,j,word,index,"NW",[matrix[i][j]],[[i,j]]):

                        #print("NW " + word + " found with start pos: " + str(i) + "," + str(j))
                        wordTotal += 1

                if checkValidPos(i,j-1):
                    if DFS(matrix,i,j-1,i,j,word,index,"N",[matrix[i][j]],[[i,j]]):
                        #print("N " + word + " found with start pos: " + str(i) + "," + str(j))
                        wordTotal += 1
                    
                if checkValidPos(i+1,j-1):
                    if DFS(matrix,i+1,j-1,i,j,word,index,"NE",[matrix[i][j]],[[i,j]]):
                        #print("NE " + word + " found with start pos: " + str(i) + "," + str(j))
                        wordTotal += 1

                if checkValidPos(i+1,j):
                    if DFS(matrix,i+1,j,i,j,word,index,"E",[matrix[i][j]],[[i,j]]):
                        #print("E " + word + " found with start pos: " + str(i) + "," + str(j))
                        wordTotal += 1

                if checkValidPos(i+1,j+1):
                    if DFS(matrix,i+1,j+1,i,j,word,index,"SE",[matrix[i][j]],[[i,j]]):
                        #print("SE " + word + " found with start pos: " + str(i) + "," + str(j))
                        wordTotal += 1

                if checkValidPos(i,j+1):
                    if DFS(matrix,i,j+1,i,j,word,index,"S",[matrix[i][j]],[[i,j]]):
                        #print("S " + word + " found with start pos: " + str(i) + "," + str(j))
                        wordTotal += 1

                if checkValidPos(i-1,j+1):
                    if DFS(matrix,i-1,j+1,i,j,word,index,"SW",[matrix[i][j]],[[i,j]]):
                        #print("SW " + word + " found with start pos: " + str(i) + "," + str(j))
                        wordTotal += 1

                if checkValidPos(i-1,j):
                    if DFS(matrix,i-1,j,i,j,word,index,"W",[matrix[i][j]],[[i,j]]):
                        #print("W " + word + " found with start pos: " + str(i) + "," + str(j))
                        wordTotal += 1
    return wordTotal


total = 0
total += findWord(fc,"XMAS")
#total += findWord(fc,"SAMX")
for line in fc:
    print(line)
for line in emptyMatrix:
    for c in line:
        print(c,end="")
    print()
print(total)