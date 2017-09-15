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

import hashlib
import getpass

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


forms = '''<form method = "GET" action = "createaccount.py">
            <p> UserName: <input type = "text" name = "UserName"> </p>
            <p> Password: <input type = "password" name = "Password"> </p>
            <input type = "submit" name = "button" value = "Create Account">
            
            </form>
        '''


print '''<DOCTYPE! = html>
            <html>
                <head>
                    <title> Account Simulator  </title>
                </head>
                <body>
                    <h1> Account Creation Simulator 2016 </h1>
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
            f.write(str(formResults.getvalue('UserName')+ ',' + hashlib.sha256(formResults.getvalue('Password')).hexdigest() + '\n'))
            #                                                   formResults.getvalue('Password')
            #                                                   hashlib.sha256(formResults.getvalue('Password')).hexdigest()
            print '''Account has been made. <br>Proceed back or to login?<br>
                <a href = "http://marge.stuy.edu/~gordon.lei/labs/lab15/createaccount.py"> Back </a> <br>
                <a href = "http://marge.stuy.edu/~gordon.lei/labs/lab15/login.py"> Login </a>
            '''
        
    
print '''</body>
        </html>'''
f.close()
