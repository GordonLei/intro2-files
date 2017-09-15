#!/usr/bin/python
print "content-type: text/html\n"

#Lei,Gordon
#Intro2,pd1
#Account Logins
#2016-05-12

import cgitb
cgitb.enable()
import cgi
formResults = cgi.FieldStorage()

f = open('data/stats.txt', 'r')
stats = f.read()
f.close()
f = open('data/death.txt', 'r')
death = f.read()
f.close()
f = open ('data/death.txt', 'w')
f.write(str(death + 1))
f.close()
if stats.split(',')[0] <= 0:
    print "<center><h1>YOU DIED </h1></center>"
    
