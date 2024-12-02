

FILENAME = "Data.txt"

def getFileContents(fn):

    fp = open(fn,"r")
    fc = fp.readlines()
    fp.close()
    return fc


RL = []
LL = []

for line in getFileContents(FILENAME):

    lineSplit = line.split("   ")
    RL.append(lineSplit[1].strip())
    LL.append(lineSplit[0].strip())

RL.sort()
LL.sort()

diffTotal = 0

for i in range(len(RL)):
    #print(i)
    print(str(LL[i]) + "   " + str(RL[i]))
    diff = abs(int(RL[i])-int(LL[i]))
    print(diff)
    diffTotal += diff
print("Diff total: " + str(diffTotal))