FILENAME = "Data.txt"

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

        a = str(sum)
        b = str(vals[index])
        c = int(a+b)

        if sum+vals[index] == ans or sum*vals[index] == ans or c == ans:

            #print("ans: ",ans)
            return True
        else:
            #print("Failed: Ans: " + str(ans) + " calculated sum: " + str((sum+vals[index])) + " " + str((sum*vals[index])))
            return False
    # elif index == len(vals)-2:
    a = str(sum)
    b = str(vals[index])
    c = int(a+b)
    #print("Ans: " + str(ans) + " C: " + str(c))

    if solver(vals,index+1,sum+vals[index],ans) or solver(vals,index+1,sum*vals[index],ans) or solver(vals,index+1,c,ans):
        return True

    # else:
    #     if solver(vals,index+1,sum+vals[index],ans) or solver(vals,index+1,sum*vals[index],ans):

    #         return True
    


fc = getFileContents(FILENAME)
fc = parseFile(fc)
total = 0


for line in fc:

    if solver(line[1],0,0,line[0]):

        total += line[0]

print(total)


