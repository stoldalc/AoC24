FILENAME = "Data.txt"
#FILENAME = "Day6\\TestData.txt"
def getFileContents(fn):
    fp = open(fn,"r")
    fc = fp.readlines()
    fp.close()
    for i in range(len(fc)):
        fc[i] = fc[i].strip()
    return fc

def formatFileContent(fc):
    
    fc = list(fc[0].strip())

    for i in range(len(fc)):
        fc[i] = int(fc[i])
    return fc



def sortData(fc):

    index = 0

    results = []

    while index < len(fc):

        file = fc[index]
        index += 1
        
        if index < len(fc):
            freeSpace = fc[index]
            results.append([file,freeSpace])
        else:
            results.append([file])
        index += 1
    
    return results


def data2DiskFormat(fc):


    result = []

    index = 0

    for file in fc:

        for i in range(int(file[0])):

            # for c in str(index):
            #     result.append(c)

            result.append(str(index))

        if len(file) == 2:
            for i in range(int(file[1])):
                result.append(".")
        index += 1
    return result

def formatedDiskPrinter(diskStr):


    print("Disk Data: ", end="")

    for bit in diskStr:
        print(bit,end="")
    print()

def deFragDisk(diskStr):


    i = 0

    endI = len(diskStr)-1

    while i < len(diskStr) and endI >= 0 and endI >= i:

        if diskStr[i] != ".":
            i += 1
        elif diskStr[i] == ".":

            if diskStr[endI] != ".":
                diskStr[i] = diskStr[endI]
                diskStr.pop(endI)
                endI -= 1
            else:
                while diskStr[endI] == ".":
                    #print("Current disk position is: ",diskStr[endI])
                    endI -= 1
                    
                diskStr[i] = diskStr[endI]
                diskStr.pop(endI)
                #print("Len of diskstr: ",len(diskStr))
                #print("endI Index: ",endI)
                endI -= 1
        #formatedDiskPrinter(diskStr)

    return diskStr


def calculateChecksum(data):

    total = 0

    index = 0

    for bit in data:

        if bit != ".":
            total += index * int(bit)
            index += 1
    print("Checksum final index: ", index)
    return total


def countBits(diskStr):

    total = 0

    for bit in diskStr:
        if bit != ".":
            total += 1
    return total


fc = getFileContents(FILENAME)

fc = sortData(fc[0])
print("Number of file pairs: ",len(fc))
diskStr = data2DiskFormat(fc)



print("Total File entrys including empty space: ",len(diskStr))
print("Total bits: ", countBits(diskStr))


#formatedDiskPrinter(diskStr)
defraggedDisk = deFragDisk(diskStr)
#print(defraggedDisk)
#formatedDiskPrinter(defraggedDisk)
print("Checksum: ",calculateChecksum(defraggedDisk))


