#!/usr/bin/python
print "content-type: text/html\n"

#Lei,Gordon
#Intro2,pd1
#Stat Change
#2016-05-16

import cgitb
cgitb.enable()
import cgi
formResults = cgi.FieldStorage()

import hashlib

directory = 'data/'
f = open((directory + 'saveFiles.txt'), 'a')

f2 = open((directory + 'saveFiles.txt'), 'r')

f3 = open((directory + 'stats.txt'), 'w')

f4 = open((directory + 'inventory.txt'), 'w')
f4.write('0,0')
f4.close()

saveFilesAble = f2.read()
saveFiles = saveFilesAble.split('\n')
saveFiles.pop()
f2.close()

UserList = []
for users in saveFiles:
    users = users.split(',')[0]
    UserList.append(users)

#print accounts

#import getpass


forms = '''<form method = "GET" action = "statChange.py">
            <p> UserName: <input type = "text" name = "UserName"> </p>
            <p> Password: <input type = "password" name = "password"> </p>
            <p> HP: <input type = "text" name = "HP"> </p>
            <p> Mana: <input type = "text" name = "mana"> </p>
            <p> Armor: <input type = "text" name = "armor"> </p>
            <p> Dodge: <input type = "text" name = "dodge"> </p>
            <input type = "submit" name = "button" value = "Create Account">
            
            </form>
        '''


print '''<DOCTYPE! = html>
            <html>
                <head>
                    <title> Stat Change  </title>
                </head>
                <body>
                    <h1> Change your Stats! </h1>
                    <p> Stats </p>
                    <table border = 1>
                        <tr>
                            <th> HP </th>
                            <th> Mana </th>
                            <th> Armor </th>
                            <th> Dodge </th>
                        </tr>
                        <tr>
                            <td> Increases the amount of hit points you have.
                                The more HP you have, the mroe htis you can take.</td>
                            <td> Increases the amount of mana you have.
                                The more mana you have, the more spells you can cast.</td>
                            <td> Armor lessens some of the damage you take.</td>
                            <td> Dodge gives you a slight chance to take no damage at all.</td>
                        </tr>
                    </table>
                </body>
                        
        '''
#print len(formResults)
if len(formResults) == 0:
    print forms
if len(formResults) > 0:
    if formResults.getvalue('UserName') in UserList:
        print '''UserName is already taken. Please go back.
                <a href = "http://marge.stuy.edu/~gordon.lei/labs/lab15/createaccount.py"> Back </a>
                '''
    elif not(formResults.getvalue('UserName') in UserList):
        if ',' in formResults.getvalue('UserName'):
            print '''Commas are invalid in UserName. <br>Please go back.<br>
                    <a href = "http://marge.stuy.edu/~gordon.lei/labs/lab15/createaccount.py"> Back </a>
                '''
        else:
            f.write(str(formResults.getvalue('UserName')+ ',' + hashlib.sha256(formResults.getvalue('Password')).hexdigest() + formResults.getvalue('HP') + ',' + formResults.getvalue('mana') + ',' + formResults.getvalue('armor') + ',' + formResults.getvalue('dodge')  + '\n'))
            #                                                   formResults.getvalue('Password')
            #                                                   hashlib.sha256(formResults.getvalue('Password')).hexdigest()
            f4.write(str(formResults.getvalue('UserName')+ ','  + formResults.getvalue('HP') + ',' + formResults.getvalue('mana') + ',' + formResults.getvalue('armor') + ',' + formResults.getvalue('dodge')  + '\n'))
            print 'Done'
    
print '''</body>
        </html>'''
f.close()
