FILENAME = "TestData.txt"
#FILENAME = "Day6\\TestData.txt"
def getFileContents(fn):
    fp = open(fn,"r")
    fc = fp.readlines()
    fp.close()
    for i in range(len(fc)):
        fc[i] = fc[i].strip()
    return fc



fc = getFileContents(FILENAME)

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



def formatedPrint(fileList):



    index = 0

    for file in fileList:

        for i in range(file[0]):
            print(index,end="")
        if len(file) == 2:
            for i in range(file[1]):
                print(".",end="")
        index += 1
    print()

def file2String(file,index):

    result = ""

    for i in range(file[0]):
        result += str(index)
    return result

def sortFiles(files):

    i = 0
    result = ""

    fragCleared = []

    print(files)

    #Step through all of the files
    while i < len(files):


        #Create the instance of the current file we are looking for 
        # we also add this index to the file and make sure we have not already looked at it
        if i not in fragCleared:
            fragCleared.append(i)

            file = files[i]
            print("Checking file with free bits: ", file[1])

            result += file2String(file,i)


            #We need to check and see if the file has botht the block size and the free space after it
            if len(file) == 2:

                #Make our index counter for our internal for loop
                j = len(files)-1

                #File we use to assist us in breakuing out of our while loop
                fileFound = False
                while j >= 0 and not fileFound:

                    #Check if the file we are looking at in our internal loop takes up the amount of space 
                    # that the file we are looking at in our i loop has behind it and  verify its not in the fragCleared list
                    #print("Comparing: " + str(files[j][0]) + str)
                    if(j not in fragCleared):
                        print("Not in defragged list: ", j)
                        if files[j][0] == file[1]:
                            fragCleared.append(j)
                            fileFound = True
                            result += file2String(files[j],j)
                            print("Index defragged: ", j)
                        elif files[j][0] < file[1]:

                            fragCleared.append(j)
                            result += file2String(files[j],j)

                            file[1] -= files[j][0]
                            j = len(files)
                            print("Index defragged: ", j)
                        

                    j -= 1
        print(result)
        #print("Positions defragged: ", fragCleared)



        i+=1
    print(result)

        



def calculateChecksum(data):

    total = 0

    for i in range(len(data)):

        total +=  i * int(data[i])
    return total


fc = formatFileContent(fc)

fileList = sortData(fc)

print(fileList)

#print(fileList)
#formatedPrint(fileList)

sortFiles(fileList)
