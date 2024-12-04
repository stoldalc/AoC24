

FILENAME = "TestData.txt"

def getFileContents(fn):

    fp = open(fn,"r")
    fc = fp.readlines()
    fp.close()
    return fc

def formatData(fc):

    results = []

    for line in fc:

        buffer = line.split(" ")
        for i in range(len(buffer)):

            buffer[i] = int(buffer[i].strip())

        results.append(buffer)
    return results

def formatedDebug(lineAtI,current,type):
    print("Failed: ")
    print("\tCurrent: " + str(current))
    print("\tline at i: " + str(lineAtI))
    print("\t" + type + " than check: " + str(lineAtI <= current))
    print("\tGap check: " + str((abs(lineAtI-current) > 3)))

def checkDec(line):
    
    
    return checkDecHelper(line,1,line[0],False)

def checkDecHelper(line,index,current,blFlag):
    
    if index >= len(line):
        return True

    if (line[index] <= current) or (abs(line[index]-current) > 3):

        if blFlag:
            return False
        
        blFlag = True
        buffer = current
        current = line[index]

        checkDecHelper(line,index+1,buffer,blFlag)
        checkDecHelper(line,index+2,current,blFlag)
    else:
        checkDecHelper(line,index+1,line[index+1],blFlag)
    return True
        

def checkInc(line):
    pass

reports = formatData(getFileContents(FILENAME))

total = 0

for report in reports:

    if checkDec(report) or checkInc(report):
        print("Report found safe: " + str(report) )
        total += 1
    else:
        print("Report found NOT safe: " + str(report) )
print(total)