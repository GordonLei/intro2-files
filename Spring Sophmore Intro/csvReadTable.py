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

data =text.split("\n")

def makeTable(allLines):
    ans = "<table> \n "
    for each in allLines: #each represents 
        ans += "\t <tr> "
        rows = each.split(",")
        for each2 in rows:
            ans += "\n \t \t <td> " + str(each2) + " </td>"
        ans += "\n \t </tr> \n"
    return ans + "</table> \n"
print makeTable(data)
