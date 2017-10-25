#!/usr/bin/python
print 'content-type: text/html'
print ''

import cgitb,cgi,hashlib,pickle,sys
cgitb.enable()

sys.path.insert(0, "../modules")
import stdStuff
sys.path.insert(0, "../modules")
import styleSheet
form = cgi.FieldStorage()

head = '''
<html>
<head>

<title>Create an account</title>

</head>
<body class = "ToastBackground">
   '''
body = ""
foot = '''
</body>
</html>
'''
directory = "../data/"
file = "users.txt"

def nameIsAvailable(L, user):
	for x in L:
		if user == x.name:
			return False
	return True

if len(form)<=1:
	body = '''
<center>
<div class = "TranslucentBox center">
    <h1 class = "title">Create account:</h1>
    <form action="createaccount.py">

    Username: <input type="text" name="username"><br>
    Password: <input type="password" name="password"><br>
    <input type="submit" value="create account" class = "buttonHover button">
</div>
<center>
    '''
else:
	userHolder = None
	
	if 'username' in form and 'password' in form:
		'''if "<" in form.getvalue("username") or ">" in form.getvalue("username"):
			body += "You can't use that character!"
		else:'''
		userReadStream = open(stdStuff.directory + stdStuff.userFile, "rb")
		userList = []
		try:
			while True:
				userList.append(pickle.load(userReadStream))
		except EOFError:
			#print "End of File"
			pass
		finally:
			userReadStream.close()
	
		if nameIsAvailable(userList, form.getvalue("username")):
			with open(stdStuff.directory + stdStuff.userFile, "a") \
			as userWriteStream:
				userWriteStream = \
				open(stdStuff.directory + stdStuff.userFile, "a")
				
				pickle.dump(
					stdStuff.User(
						stdStuff.deleteBrackets(form.getvalue("username")),
						hashlib.sha256(form.getvalue("password"))
							.hexdigest()),
					userWriteStream)
		
			body += \
			'''<center>
<div class = "TranslucentBox center">Successfully added. <a href="login.py"> Click here to log in</a>.<br></div></center>'''
		else:
			body += '''<center>
<div class = "TranslucentBox center">Username already taken!</div></center>'''
	else:
		body += '''<center>
<div class = "TranslucentBox center">Please use the form!</div></center>'''

print head
print body
print foot
