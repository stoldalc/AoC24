# Python program to find all the matches
import re

FILENAME = "TestData.txt"

def getFileContents(fn):

    fp = open(fn,"r")
    fc = fp.readlines()
    fp.close()
    return fc

fc = getFileContents(FILENAME)
 
subject = fc[0].strip()
 
# Template instantiations for
# extracting the matching pattern.

searchExp = "mul\([1-9][0-9]{0,2},[1-9][0-9]{0,2}\)"

match = re.search(searchExp, subject)
#i = 1
 
while match:
    print("Match Found: ", match.group(0))
    print("and it is found at position", match.start())
    #i += 1
 
    # suffix to find the rest of the string.
    subject = subject[(match.end()):]
    match = re.search(searchExp, subject)