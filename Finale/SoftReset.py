#!/usr/bin/python
print 'content-type: text/html'
print ''
import cgitb
cgitb.enable()
print "Attempt to write file<br>"

directory = "../data/"
fileN = "counter.txt"

f = open(directory + fileN,'w')
f.write("0")
f.close()

f = open(directory + 'groups.txt','w')
f.close()
f = open(directory + 'currentGroup.txt','w')
f.close()
f = open(directory + 'groupsName.txt','w')
f.close()

print "Completed attempt<br>"

