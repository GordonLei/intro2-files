#!/usr/bin/python
print "content-type: text/html\n"

#Lei,Gordon
#Intro2,pd1
#Account Logins
#2016-05-12

import cgi
formResults = cgi.FieldStorage()
import cgitb
cgitb.enable()
import hashlib


directory = 'data/'
f = open((directory + 'users.txt'), 'a')
#f.write('Ay')


f2 = open((directory + 'users.txt'), 'r')
accountable = f2.read()
accounts = accountable.split('\n')
accounts.pop()
f2.close()

UserList = []
for users in accounts:
    users = users.split(',')[0]
    UserList.append(users)
#print accounts

#import getpass


forms = '''<form method = "GET" action = "login.py">
            <p> UserName: <input type = "text" name = "UserName"> </p>
            <p> Password: <input type = "password" name = "Password"> </p>
            <input type = "submit" name = "button" value = "Login">
            
            </form>
        '''


print '''<DOCTYPE! = html>
            <html>
                <head>
                    <title> Loginerino </title>
                </head>
                <body>
                    <h1> Login Simulator 2016 </h1>
        '''
#print len(formResults)
if len(formResults) == 0:
    print forms
if len(formResults) > 0:
    if (formResults.getvalue('UserName') + ',' + hashlib.sha256(formResults.getvalue('Password')).hexdigest()) in accounts:
        #                                       formResults.getvalue('Password')
        print '''Success!'''
    else:
        print '''Login Failed'''
        
    
print '''</body>
        </html>'''
f.close()
