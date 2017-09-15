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
f3 = open((directory + 'saveFiles.txt'), 'a')

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
styleSheet = '''
            <style>
            .HoverColor:hover {background-color: cyan;
                                }
            .Button {text-align:center;
                    width:150px;
                    height:100px;}
            </style>
            '''

forms = '''<form method = "GET" action = "createaccount.py">
            <p> UserName: <input type = "text" name = "UserName"> </p>
            <p> Password: <input type = "password" name = "Password"> </p>
            <input type = "submit" name = "button" value = "Create Account">
            
            </form>
        '''

print styleSheet
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
                <a href = "http://marge.stuy.edu/~gordon.lei/labs/Final%20Project%20Spring%20Intro%202/2016-05-19/createaccount.py"> Back </a>
                '''
    elif not(formResults.getvalue('UserName') in UserList):
        if ',' in formResults.getvalue('UserName'):
            print '''Commas are invalid in UserName. <br>Please go back.<br>
                    <a href = "http://marge.stuy.edu/~gordon.lei/labs/Final%20Project%20Spring%20Intro%202/2016-05-19/createaccount.py"> Back </a>
                '''
        else:
            f.write(str(formResults.getvalue('UserName')+ ',' + hashlib.sha256(formResults.getvalue('Password')).hexdigest() + '\n'))
            f3.write(str(formResults.getvalue('UserName')+ ',' + hashlib.sha256(formResults.getvalue('Password')).hexdigest()))
            #                                                   formResults.getvalue('Password')
            #                                                   hashlib.sha256(formResults.getvalue('Password')).hexdigest()
            print '''Account has been made. <br>Proceed back or to game?<br>
                <form action = "http://marge.stuy.edu/~gordon.lei/labs/Final%20Project%20Spring%20Intro%202/2016-05-19/createaccount.py">
                    <input type = "submit" class = "HoverColor Button" value = "Back"> 
                </form>
                <form action = "statChange.py">
                    <input type = "submit" class = "HoverColor Button" value = "Enter the World of Text Souls"> 
                </form>
            '''
        
    
print '''</body>
        </html>'''
f.close()
f2.close()
