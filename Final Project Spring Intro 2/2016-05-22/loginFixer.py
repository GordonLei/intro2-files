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
import random
import os
ip = os.environ["REMOTE_ADDR"]

directory = 'data/'

f = open((directory + 'stats.txt'), 'w')
f.close()
f = open((directory + 'inventory.txt'), 'w')
f.close()
f = open((directory + 'death'), 'w')
f.close()

f = open((directory + 'users.txt'), 'a')
#f.write('Ay')



f2 = open((directory + 'users.txt'), 'r')
accountable = f2.read()
accounts = accountable.split('\n')
accounts.pop()
f2.close()

f3 = open((directory + 'loggedin.txt'), 'a')

f4 = open((directory + 'loggedin.txt'), 'r')
loggedinAble = f4.read()
loggedin = loggedinAble.split('\n')
loggedin.pop()
f4.close()

f5 = open((directory + 'loggedin.txt'), 'w')
UserList = []
for users in accounts:
    users = users.split(',')[0]
    UserList.append(users)

LoggedInList = []
for users in loggedin:
    users = users.split(',')[0]
    LoggedInList.append(users)
#print accounts

#import getpass




    
def writeOrReplace(filename,username,number,IP):
    #check if you need to remove old values
    f = open(filename,'r').read().split("\n");
    data = [each.split(',') for each in f]
    write = False
    for i in range(len(data))[::-1]:
        if data[i]==['']:
            write = True
            data.pop(i)
        elif data[i][0]==username:
            data.pop(i)
            write = True
    ##remove a line if needed
    if write:
        res = ""
        for each in data:
            res+= ",".join(each)+"\n"
        f = open(filename,'w')
        f.write(res)
        f.close()
    #append the line to the file
    f = open(filename,'a')
    f.write(username+","+str(number)+","+str(IP)+"\n")
    f.close()


    

forms = '''<form method = "GET" action = "loginFixer.py">
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
number = random.randint(0,1000000000)
if len(formResults) == 0:
    print forms
if len(formResults) > 0:
    if (formResults.getvalue('UserName') + ',' + hashlib.sha256(formResults.getvalue('Password')).hexdigest()) in accounts:
        #                                       formResults.getvalue('Password')
        writeOrReplace((directory + 'users.txt'), formResults.getvalue('UserName'), number, str(ip))
        print '''Success!'''
        print "<br> <a href = 'http://marge.stuy.edu/~gordon.lei/labs/lab16/main.py?UserName=" + formResults.getvalue('UserName') + '''&id=''' + str(number) + "'> Main page </a>"
    else:
        print '''Login Failed'''
        
    
print '''</body>
        </html>'''
f.close()
f3.close()
f5.close()
