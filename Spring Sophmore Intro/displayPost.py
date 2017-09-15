#!/usr/bin/python
#print "content-type: text/html\n"


wall = open("data/wall.txt", 'r')
wallRead = wall.read()
ListOfPosts = (wallRead.split('\n')).pop()
wall.close()
for post in ListOfPosts:
    post = post.split('^')
    print '<h1>'+str(post[0]) + '</h1><p>' + str(post[2]) + '</p>'

