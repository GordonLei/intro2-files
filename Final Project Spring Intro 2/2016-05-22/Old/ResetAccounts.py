#!/usr/bin/python
print "content-type: text/html\n"

#Lei,Gordon
#Intro2,pd1
#Erase Save Files
#2016-05-16

import cgi
formResults = cgi.FieldStorage()
import cgitb

directory = 'data/'
f = open((directory + 'saveFiles.txt'), 'w')
f.write('''
        #Data is read as: UserName,Password,HP,Mana,Armor,Dodge,EXP,[HP Potion, Mana Potion]
        '''
f.close()

