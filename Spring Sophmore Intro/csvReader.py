#!/usr/bin/python
print "content-type: text/html\n"

#Lei,Gordon
#Intro2,pd.1
#CSV For Loop HW
#2016-04-08

text = """a,b,c
d,e,f"""
text2="""fish,dog,cat
1,99,3
o o,this is, so strange
"""
#f = open("table.csv", "r")
#text = f.read()
#f.close()

data =text2.split("\n")

def makeTable(allLines):
    ans = "<html>\n<head> Cool </head>\n<body>\n<table border = '1'> \n "
    for each in allLines: #each represents 
        ans += "\t <tr> "
        rows = each.split(",")
        for each2 in rows:
            ans += "\n \t \t <td> " + str(each2) + " </td>"
        ans += "\n \t </tr> \n"
    ans += "</table> \n</body>\n</html>"
    return ans 
#print makeTable(data)

#2016-04-18 and 2016-04-19
t = '''1,2,3
4,5,6
8,fish,10'''

t = '''1,2,3
4,5,6
8,"fish, fish",10'''
MyL = [ ['1','2','3'], ['"fish','cakes"',"oops","hi"], ['"fish','cakes','etc"',"hi",'hi2']]




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

#MyL = [ ['1','2','3'], ['"fish','cakes"',"oops","hi"], ['"fish','cakes','etc"',"hi",'hi2']]
#print MyL
#fixCommas(MyL)
#print MyL

def makeList(s):
    ans = []
    allLines = s.split("\n")
    for lines in allLines:
        line = lines.split(",")
        ans.append(line)
    fixCommas(ans)
    ans =  [x for x in ans if x != []]
    return ans

#print makeList(text[0:3])


satList = makeList(text[:451])
#print satList

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
