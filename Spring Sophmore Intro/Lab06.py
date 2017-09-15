#!/usr/bin/python
print "content-type: text/html\n"

#Lei,Gordon
#Intro2,pd1
#Lab06
#2016-03-17


#==============================================================================#
# Below are PyLab05 Code. Lab06 is at the very bottom after a double commented bar line thing(in other words two of the commented bars shown above this line
def numToWords9(i):
    if i == 1:
        return "one"
    if i == 2:
        return "two"
    if i == 3:
        return "three"
    if i == 4:
        return "four"
    if i == 5:
        return "five"
    if i == 6:
        return "six"
    if i == 7:
        return "seven"
    if i == 8:
        return "eight"
    if i == 9:
        return "nine"
    if i == 0:
        return ""

#numToWords9(4) --> 'four'
def numToWords99(i):
    word = ""
    n = i % 10
    q = (i / 10)
    if (i/10) < 1:
        numToWords9 (i)
    elif (i/10) == 1:
        if n == 0:
            return "ten"
        if n == 1:
            return "eleven"
        if n == 2:
            return "twelve"
        if n == 3:
            return "thirteen"
        if n == 4:
            return "fourteen"
        if n == 5:
            return "fifteen"
        if n == 6:
            return "sixteen"
        if n == 7:
            return "seventeen"
        if n == 8:
            return "eighteen"
        if n == 9:
            return "nineteen"
    else:
        if q > 1:
            if q == 2:
                word = word + "twenty"
            elif q == 3:
                word = word + "thirty"
            elif q == 4:
                word = word + "forty"
            elif q == 5:
                word = word + "fifty"
            elif q == 8:
                word = word + "eighty"
            else:
                word = numToWords9(q) + "ty"
    word = word + " " +numToWords9 (i % 10)
    return word

#>>> numToWords99 (23)
#'twenty three'
#>>> numToWords99 (90)
#'ninety '
        
def numToWords999(i):
    word = ""
    q = (i/100)
    if (i/100) == 0:
        word = word + numToWords99(i)
        return word
    else:
        word = word + numToWords9 (q) + " hundred " + numToWords99(i - ((i/100) * 100))
        return word
#numToWords999 (967) --> 'nine hundred sixty seven'

def numToString(x):
    if x<0:
        return "negative " + numToString(abs(x))
    if x==0:
        return "zero"
    else:
        return recToWordsBig(x)
#numToString(597) --> 'five hundred ninety seven'
#numToString(-484) --> 'negative four hundred eightty four'


#Recursive numToWords999 [The Actual/Fixed Version]
def recursiveToWords999(i):
    n = 10
    unit = 0
    word = ""
    number = i
    number2 = i
    while number>=10:
        number = number/n
        unit = unit + 1
    while unit >= 0:
        if unit == 1:
            word = word + numToWords99(number2)
        if unit == 2:
            word = word + numToWords9((number2- (number2%(n**2)))/(n**2)) + " hundred "
        number2 = number2%(10**unit)
        unit = unit - 1
    return word

#>>> recursiveToWords999(23) -->
#'twenty three'

#>>> recursiveToWords999(765) -->
#'seven hundred sixty five'

#==================================================================================================================================#
def numToWordsBig(i):
    n = 1000
    unit = 0
    word = ""
    number = i
    while number>=1000:
        number = number/n
        unit = unit + 1
    if unit >= 0:
        if unit == 0:
            word = word + numToWords999(i) 
        if unit == 1:
            word = word + numToWords999((i - (i%1000))/1000) + " thousand " + numToWords999(i%1000)
        if unit == 2:
            word = word + numToWords999((i - (i%1000000))/1000000) + " million " + numToWords999(((i%1000000) - (i%1000))/1000) + " thousand " + numToWords999(i%1000)
    return word


#>>> numToWordsBig(123456789) -->
#'one hundred twenty three million four hundred fifty six thousand seven hundred eighty nine'
#>>> numToWordsBig(12345)
#'twelve thousand three hundred forty five'

def recToWordsBig(i):
    n = 1000
    unit = 0
    word = ""
    number = i
    number2 = i
    while number>=1000:
        number = number/n
        unit = unit + 1
    while unit >= 0:
        if unit == 0:
            word = word + numToWords999(i%n) 
        if unit == 1:
            word = word + numToWords999((number2- (number2%n))/n) + " thousand " 
        if unit == 2:
            word = word + numToWords999((number2- (number2%(n**2)))/(n**2)) + " million "
        if unit == 3:
            word = word + numToWords999((number2- (number2%(n**3)))/(n**3)) + " billion "
        if unit == 4:
            word = word + numToWords999((number2- (number2%(n**4)))/(n**4)) + " trillion "
        if unit == 5:
            word = word + numToWords999((number2- (number2%(n**5)))/(n**5)) + " quadrillion "
        if unit == 6:
            word = word + numToWords999((number2- (number2%(n**6)))/(n**6)) + " quintillion "
        number2 = number2%(n**unit)
        unit = unit - 1      
    return word
    
#>>> recToWordsBig(1234567892345)
#' one trillion two hundred thirty four billion five hundred sixty seven million eight hundred ninety two thousand three hundred forty five'

#==============================================================================
#==============================================================================
#The Start of Lab06
import random

def startPage(title):
    return "<!DOCTYPE html>\n<html>\n <head><title>" + str(title) + "</title></head>\n <body>\n" 

def endPage():
    return "</body> \n </html>"

def makeRow():
    randXnumber = random.randint(-999,999)
    randYnumber = random.randint(-999999,999999)
    randZnumber = random.randint(-999999999,999999999)
    
    randX = "\n <tr>" + "\n <td> " + str(randXnumber) + " </td>" + "\n <td> " + numToString(randXnumber) + " </td> \n </tr> \n"
    randY = "\n <tr>" + "\n <td> " + str(randYnumber) + " </td>" + "\n <td> " + numToString(randYnumber) + " </td> \n </tr> \n"
    randZ = "\n <tr>" + "\n <td> " + str(randZnumber) + " </td>" + "\n <td> " + numToString(randZnumber) + " </td> \n </tr> \n"
    row = randX + randY + randZ 
    #numRows = 3
    #randX = random.randint(-999,999)
    #randY = random.randint(-999999,999999)
    #randZ = random.randint (-999999999,999999999)
    #choice = 1
    #while numRows > 0:
    #    if choice == 1:
    #        choice = randX
    #    if choice == 2:
    #        choice = randY
    #    if choice == 3:
    #        choice = randZ
    #    numSeg = "\n <td>" + numToString(choice) + "</td>"
    #    row = row + numSeg
    #    numRows = numRows - 1
    #    choice = choice + 1
    #row = row + "\n </tr> \n" 
    return row

def makeTableHead():
    return "<tr> \n <th> Number </th> \n <th> How To Say The Number </th>  \n </tr>"
    
def makeTable():
    Table = "<table border = '1'>" + "<tr> \n <th> Number </th> \n <th> How To Say The Number </th>  \n </tr>" + makeRow()+ "</table>"
    return Table

print startPage("Numbers to Words")
print makeTable()
print endPage()

