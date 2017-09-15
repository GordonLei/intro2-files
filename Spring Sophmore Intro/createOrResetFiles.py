#!/usr/bin/python
print 'content-type: text/html'
print ''
import cgitb
cgitb.enable()
print "Attempt to write file<br>"

directory = "../data/"
fileN = "posts.txt"

f = open(directory + fileN,'w')
f.close()
f = open(directory + 'comments.txt','w')
f.close()
f = open(directory + 'postID.txt','w')
f.close()
f = open(directory + 'postCounter.txt','w')
f.write('0')
f.close()
print "Completed attempt<br>"
