#!/usr/bin/python
print "content-type: text/html\n"

#Lei,Gordon
#Intro2,pd1
#Account Logins
#2016-05-19

import cgitb
cgitb.enable()
import os
os.path.abspath(os.curdir)

directory = 'images/'
#========================== Style Sheet =====================
styleSheet = '''
            <style>
            .HoverColor:hover {background-color: cyan;
                                }
            .Button {text-align:center;
                    width:150px;
                    height:100px;}
            </style>
            '''
#========================= Html ==========================
beginning =  '''
            <DOCTYPE! = html>
            <html>
                <head>
                    <title> Dank Souls  3.141592653589793238462643383279502884197WhyAreYouStillLookingAtThis </title>
                </head>'''
body = '''
                <body>
                    <center> <h1> Dank Souls 3.14 </h1> </center>
                    <center> <img src ="''' + directory + 'TextSouls301.jpg"' + '/>' + '''
                    <br>
                    <form action = 'createaccount.py'>
                        <input type = "submit" class = "HoverColor Button" value = "New Game"> 
                    </form>
                    <form action = 'loginFixer.py'>
                        <input type = "submit" class = "HoverColor Button" value = "Continue Game"> 
                    </form>
                    <form>
                        <input type = "submit" class = "HoverColor Button" value = "Reviews"> 
                    </form>
                    
        '''

    
end =  '''</body>
        </html>'''

#=============================Print ===========================
print styleSheet
print beginning
print body
print end
