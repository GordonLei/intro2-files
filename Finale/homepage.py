#!/usr/bin/python
print 'content-type: text/html'
print ''

import cgitb,cgi,sys,os,Cookie,pickle
cgitb.enable()
sys.path.insert(0, "../modules")
import stdStuff
sys.path.insert(0, "../modules")
import styleSheet

form = cgi.FieldStorage()

head = '''<!DOCTYPE html>
<html>
<head>
	<title>Homepage</title>
</head>
<body class ="ToastBackground">
   '''
body = """
<center>
<div class = 'translucentBox baguette'>
        <div class = "baguette">
                <h1 class = 'title baguette'>Planet of the Toast: The Social Network</h1>
        </div>
</div>
        


<div class = "center translucentBox">
                <form method="GET" action="createaccount.py">
                        <input name="new" type="submit" value="Create Account" class="buttonHover button">
                </form>
                        
                <form method="GET" action="login.py">
                        <input name="login" type="submit" value="Login" class="buttonHover button">
                </form>

</div></center>
"""
foot = '''
</body>
</html>
'''

if "logOut" in form:
	logStream = open(stdStuff.directory + stdStuff.logFile, "w")
	logStream.write("")
	logStream.close()


print head
print body
print foot
