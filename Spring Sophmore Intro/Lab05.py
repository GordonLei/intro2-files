#!/usr/bin/python
print "content-type: text/html\n"

#Lei,Gordon
#Intro2,pd1
#Lab05
#2016-03-10

def startPage(title):
    return "<!DOCTYPE html>\n<html>\n <head><title>" + str(title) + "</title></head>\n <body>\n" 

#startPage("WOWOWOWOWOW")
    
def makeRow(numCols,startValue):
    row =  "<tr>"
    while numCols > 0:
        numSeg = "\n <td>" + str(startValue) + "</td>"
        row = row + numSeg
        numCols = numCols - 1
        startValue = startValue + 1
    row = row + "\n </tr> \n" 
    return row

def makeTable(Rows,Cols,startValue):
    print "<table border = '1'>"
    Table = ""
    while Rows > 0:
        Table = Table + str(makeRow(Cols,startValue))
        Rows  = Rows - 1
        startValue = startValue + Cols
    Table = Table + "</table>"
    return Table
    #print Table

#makeTable(4,2,133)
#makeRow(1,2)
#makeRow (2,12)
#makeRow (3,2)

def endPage():
    return "</body> \n </html>"


#print startPage("ASCII")
#print makeTable (3,4,5)
#print endPage



print startPage("ASCII")
print makeTable (14,16,32)
print endPage


    
