# Python program to find all the matches
import re

FILENAME = "Data.txt"

def getFileContents(fn):

    fp = open(fn,"r")
    fc = fp.readlines()
    fp.close()
    return fc

def parseMult(match):

    nums = match.split("l")[1]
    nums = nums.strip("(")
    nums = nums.strip(")")
    nums = nums.split(",")
    
    return int(nums[0])*int(nums[1])

def combiner(fc):

    result = ""

    for line in fc:
        result += line
    return result


fc = getFileContents(FILENAME)
 
subject = combiner(fc)
 
# Template instantiations for
# extracting the matching pattern.

searchExp = "mul\([1-9][0-9]{0,2},[1-9][0-9]{0,2}\)"

matchs = re.findall(searchExp, subject)


rTotal = 0
halt = False
for match in matchs:

    rTotal += parseMult(match)

print(rTotal)
