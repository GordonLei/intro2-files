#!/usr/bin/python
#print "content-type: text/html\n"

#Lei,Gordon
#Intro2,pd1
#Account Logins
#2016-05-12

import cgitb
cgitb.enable()
import cgi
formResults = cgi.FieldStorage()

directory = 'data/'
#Read Inventory
f = open((directory + 'inventory.txt'), 'r')
inventory = f.read()
f.close()
#Read Stats
f2 = open((directory + 'stats.txt'), 'r')
stats = f2.read()
f2.close()
#Read StyleSheet
f3 = open((directory + 'StatsStyleSheet.txt'), 'r')
style = f3.read()
f3.close()

f4 = open((directory + 'saveFiles.txt'), 'r')
userName = f4.read()
userName = userName.split(',')[0]
f4.close()
#print len(formResults)
print style
print '''
    <html>
    <body>
        <table class = "inventory">
            <tr>
                <td> HP Potions: </td>
                <td>''' + inventory.split(',')[0] + '''
                </td>
            </tr>
            <tr>
                <td> Mana Potions: </td>
                <td> ''' + inventory.split(',')[1] + '''
                </td>
            </tr>
        </table>
        <table class = "stats"
            <tr>
                <td>''' + userName + '''
                </td>
            </tr>
            <tr>
                <td>HP: ''' + stats.split(',')[0] + '''
                </td>
            </tr>
            <tr>
                <td>Mana: ''' + stats.split(',')[1] + '''
                </td>
            </tr>
            <tr>
                <td>Armor: ''' + stats.split(',')[2] + '''
                </td>
            </tr>
        </table>'''
            
                 
                
print '''</body>
        </html>'''

