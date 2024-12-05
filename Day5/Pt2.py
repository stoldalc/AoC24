FILENAME = "Data.txt"

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

rules = sorted(rules, key=lambda x: x[0])
#print(rules)
total = 0
pageCount = 0
for page in pages:

    

    i = 0
    pagePassed = False
    while i < len(rules):
    #for rule in rules:
        #Verify both elements of the rule exist in the page
        if (rules[i][0] in page) and (rules[i][1] in page):
        
            if page.index(rules[i][0]) > page.index(rules[i][1]):
                pagePassed = True
                buffer = page[page.index(rules[i][0])]
                page[page.index(rules[i][0])] = page[page.index(rules[i][1])]
                page[page.index(rules[i][1])] = buffer
                i = 0
            else:
                i += 1
        else:
            i += 1
        #print("Scanning rule: " + str(i) + " of " + str(len(rules)))
    #print("Completed page: " + str(pageCount) + " of " + str(len(pages)))
    pageCount += 1

    if pagePassed:
        total += getPageMiddle(page)

print(total)
