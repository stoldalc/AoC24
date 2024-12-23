

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


def checkDec(line):

    current = line[0]

    for i in range(1,len(line)):
        if line[i] >= current or (abs(line[i]-current) > 3):
            return False
        current = line[i]
    return True

def checkInc(line):

    current = line[0]

    for i in range(1,len(line)):
        if line[i] <= current or (abs(line[i]-current) > 3):
            return False
        current = line[i]
    return True

reports = formatData(getFileContents(FILENAME))

total = 0

for report in reports:

    if checkDec(report) or checkInc(report):
        print("Report found safe: " + str(report) )
        total += 1
print(total)

#print(checkDec(reports[5]))