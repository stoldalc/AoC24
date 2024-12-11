

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

def checkDec(line,levelPassed):

    current = line[0]
    for i in range(1,len(line)):

        if line[i] >= current or (abs(line[i]-current) > 3):
            # print("Case failed")
            # print("Logic statments:")
            # print("\tline[i] >= current: " + str(line[i] >= current) + " abs(line[i]-current) > 3" + str(abs(line[i]-current) > 3))
            # print("Print level Stauts: ",levelPassed)
            if not levelPassed:

                #Remove current
                buffer1 = line.copy()
                buffer1.pop(buffer1.index(current))

                #Remove index item
                buffer2 = line.copy()
                buffer2.pop(buffer2.index(line[i]))

                if i+1 < len(line):
                    buffer3 = line.copy()
                    buffer3.pop(buffer2.index(line[i+1]))
                    if checkInc(buffer1,True) or checkInc(buffer2,True) or checkInc(buffer3,True):
                        return True
                    else:
                        return False
                else:
                    if checkInc(buffer1,True) or checkInc(buffer2,True):
                        return True
                    else:
                        return False
            else:
                return False
        current = line[i]
    return True




def checkInc(line,levelPassed):

    if levelPassed:
        print("\tAdjusted Line: ",line)

    current = line[0]
    for i in range(1,len(line)):

        if line[i] <= current or (abs(line[i]-current) > 3):
                # print("Case failed")
                # print("Logic statments:")
                # print("\tline[i] <= current: " + str(line[i] <= current ) + " abs(line[i]-current) > 3" + str(abs(line[i]-current) > 3))
                # print("Print level Stauts: ",levelPassed)
                if not levelPassed:

                    #Remove current
                    buffer1 = line.copy()
                    buffer1.pop(buffer1.index(current))

                    #Remove index item
                    buffer2 = line.copy()
                    buffer2.pop(buffer2.index(line[i]))

                    if i+1 < len(line):
                        buffer3 = line.copy()
                        buffer3.pop(buffer2.index(line[i+1]))
                        if checkInc(buffer1,True) or checkInc(buffer2,True) or checkInc(buffer3,True):
                            return True
                        else:
                            return False
                    else:
                        if checkInc(buffer1,True) or checkInc(buffer2,True):
                            return True
                        else:
                            return False
                else:
                    return False
        current = line[i]
    return True

reports = formatData(getFileContents(FILENAME))

total = 0

for report in reports:

    if checkDec(report,False) or checkInc(report,False):
        print("Report found safe: " + str(report) )
        total += 1
    else:
        print("Report found NOT safe: " + str(report) )

print("Print total safe reports: ",total)

#print(checkDec(reports[5]))