#!/usr/bin/python
print "content-type: text/html\n"

#Lei,Gordon
#Intro2,pd.1
#CSV For Loop HW
#2016-04-08
#2016-04-18 and 2016-04-19
f = open("SAT.csv", "r")
text = f.read()
f.close()


def fixCommas(L):
    for inner in L:
        i=0
        while i < len(inner):
            res = ''
            if inner[i][0]=='"':
                while inner[i][-1] != '"' and i<len(inner):
                    res += inner[i]+","
                    inner.pop(i)
                inner[i]=(res+inner[i]).strip('"')
            i+=1

def makeList(s):
    ans = []
    allLines = s.split("\n")
    for lines in allLines:
        line = lines.split(",")
        ans.append(line)
    fixCommas(ans)
    ans =  [x for x in ans if x != []]
    return ans
satList = makeList(text[:451])
def makeTableHead():
    html = "<table border = '1'>"
    return html

def makeTableBody(L):
    table = ""
    for OneList in L:
        table += "\t <tr> "
        for element in OneList:
            table += " <td> " + str(element) + " </td> "
        table += " </tr> \n"
    return table
#print makeTableBody(satList)

def makeTableClose():
    html = "</table>"
    return html

def startPage():
    htmlTags = "<html>"
    return htmlTags


def endPage():
    htmlTags = "</html>"
    return htmlTags

print startPage()
print makeTableHead()
print makeTableBody(satList)
print makeTableClose()
print endPage()
