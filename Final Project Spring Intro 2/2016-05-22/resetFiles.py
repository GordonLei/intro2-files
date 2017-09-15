#!/usr/bin/python
print 'content-type: text/html'
print ''
import cgitb
cgitb.enable()
print "Attempt to write file<br>"
directory = "data/"
f = open(directory+"saveFiles.txt",'w')
f.close()
f = open(directory+"loggedin.txt",'w')
f.close()
f = open(directory+"stats.txt",'w')
f.close()
f = open(directory+"inventory.txt",'w')
f.close()
f = open(directory+"death.txt",'w')
f.close()
print "Completed attempt<br>"
