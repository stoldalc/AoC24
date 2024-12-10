FILENAME = "TestData.txt"

def getFileContents(fn):
    fp = open(fn,"r")
    fc = fp.readlines()
    fp.close()
    for i in range(len(fc)):
        fc[i] = fc[i].strip()
    return fc

def parseFile(fc):

    results = []

    for line in fc:

        ans = int(line.split(":")[0])
        vals = line.split(":")[1]
        vals = vals.strip()
        vals = vals.split(" ")
        vals = [int(x) for x in vals]

        results.append([ans,vals])

    return results


def solver(vals,index,sum,ans):

    #Our exit case
    if index == len(vals)-1:

        if (sum+vals[index] == ans) or (sum*vals[index] == ans):
            return True
        else:
            return False
        
    if solver(vals,index+1,sum+vals[index],ans) or solver(vals,index+1,sum*vals[index],ans):

        return True
    


fc = getFileContents(FILENAME)
fc = parseFile(fc)
total = 0


for line in fc:

    if solver(line[1],0,0,line[0]):

        total += line[0]

print(total)



