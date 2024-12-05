

FILENAME = "Data.txt"

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

    current = line[0]
    badLevel = False

    #for i in range(1,len(line)):
    i = 1
    while i < len(line):
        if line[i] >= current or (abs(line[i]-current) > 3):

            if not badLevel:
                print("DEC - Removing: " + str(current))
                badLevel = True
                current = line[i]
                i += 1

                if i >= len(line):
                    return True 
                if line[i] >= current or (abs(line[i]-current) > 3):
                    #formatedDebug(line[i],current,"greater")
                    return False

            else:
                #formatedDebug(line[i],current,"greater")
                return False
        else:
            current = line[i]
            i += 1
    return True


def checkInc(line):

    current = line[0]
    badLevel = False
    #for i in range(1,len(line)):
    i = 1
    while i < len(line):
    
        if line[i] <= current or (abs(line[i]-current) > 3):
            if not badLevel:
                print("INC - Removing: " + str(current))
                badLevel = True
                current = line[i]
                i += 1


                if i >= len(line):
                    return True 

                if line[i] <= current or (abs(line[i]-current) > 3):
                    #formatedDebug(line[i],current,"less")
                    return False

            else:
                #formatedDebug(line[i],current,"less")
                return False
        else:
            current = line[i]
            i += 1
            
    return True

reports = formatData(getFileContents(FILENAME))

total = 0

for report in reports:

    if checkDec(report) or checkInc(report):
        print("Report found safe: " + str(report) )
        total += 1
    else:
        print("Report found NOT safe: " + str(report) )
print(total)

#print(checkDec(reports[5]))