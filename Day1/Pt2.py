

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

Total = 0

for i in range(len(LL)):
    #print(str(LL[i]) + "   " + str(RL[i]))
    Total += int(LL[i]) * RL.count(LL[i])
    #print(RL.count(LL[i]))

print("Total: " + str(Total))