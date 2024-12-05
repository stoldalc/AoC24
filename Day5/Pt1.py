FILENAME = "TestData.txt"

def getFileContents(fn):
    fp = open(fn,"r")
    fc = fp.readlines()
    fp.close()
    for i in range(len(fc)):
        fc[i] = fc[i].strip()
    return fc



fc = getFileContents(FILENAME)


splitIndex = fc.index("")

rules = fc[:splitIndex]
pages = fc[splitIndex+1:]


for i in range(len(pages)):

    pages[i] = pages[i].split(",")
    for j in range(len(pages[i])):
        pages[i][j] = int(pages[i][j])

#print(pages)

def generateRule(rule):
    rule = rule.split("|")
    return [int(rule[0]),int(rule[1])]

def getPageMiddle(page):
    return page[int(len(page)/2)]

for i in range(len(rules)):
    rules[i] = generateRule(rules[i])


total = 0
for page in pages:

    pagePassed = False
    for rule in rules:
        #Verify both elements of the rule exist in the page
        if (rule[0] in page) and (rule[1] in page):
        
            if page.index(rule[0]) > page.index(rule[1]):
                pagePassed = True
                buffer = page[page.index(rule[0])]
                page[page.index(rule[0])] = page[page.index(rule[1])]
                page[page.index(rule[1])] = buffer

    if pagePassed:
        total += getPageMiddle(page)

print(total)






    



