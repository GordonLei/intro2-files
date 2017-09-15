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
#from ButtonSheet import styleSheet

styleSheet = '''<style>
            .HoverColor:hover {background-color: cyan;
                                }
            .Button {text-align:center;
                    width:150px;
                    height:100px;}
            </style>'''
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
print styleSheet

forms = '''<form method = "GET" action = "statChange.py">
            <p> HP: <select name ="HP" size = "1">
                        <option>1</option>
                        <option>2</option>
                        <option>3</option>
                        <option>4</option>
                        <option>5</option>
                        <option>6</option>
                        <option>7</option>
                        <option>8</option>
                        <option>9</option>
                        <option>10</option>
                        <option>11</option>
                        <option>12</option>
                        <option>13</option>
                        <option>14</option>
                        <option>15</option>
                        <option>16</option>
                        <option>17</option>
                        <option>18</option>
                        <option>19</option>
                        <option>20</option>
                        <option>21</option>
                        <option>22</option>
                        <option>23</option>
                        <option>24</option>
                        <option>25</option>
                        <option>26</option>
                        <option>27</option>
                        <option>28</option>
                        <option>29</option>
                        <option>30</option>
                    </select>
                </p>
            <p> Mana: <select name ="Mana" size = "1">
                        <option>1</option>
                        <option>2</option>
                        <option>3</option>
                        <option>4</option>
                        <option>5</option>
                        <option>6</option>
                        <option>7</option>
                        <option>8</option>
                        <option>9</option>
                        <option>10</option>
                        <option>11</option>
                        <option>12</option>
                        <option>13</option>
                        <option>14</option>
                        <option>15</option>
                        <option>16</option>
                        <option>17</option>
                        <option>18</option>
                        <option>19</option>
                        <option>20</option>
                        <option>21</option>
                        <option>22</option>
                        <option>23</option>
                        <option>24</option>
                        <option>25</option>
                        <option>26</option>
                        <option>27</option>
                        <option>28</option>
                        <option>29</option>
                        <option>30</option>
                    </select>
                </p>
            <p> Armor:<select name ="Armor" size = "1">
                        <option>1</option>
                        <option>2</option>
                        <option>3</option>
                        <option>4</option>
                        <option>5</option>
                        <option>6</option>
                        <option>7</option>
                        <option>8</option>
                        <option>9</option>
                        <option>10</option>
                        <option>11</option>
                        <option>12</option>
                        <option>13</option>
                        <option>14</option>
                        <option>15</option>
                        <option>16</option>
                        <option>17</option>
                        <option>18</option>
                        <option>19</option>
                        <option>20</option>
                        <option>21</option>
                        <option>22</option>
                        <option>23</option>
                        <option>24</option>
                        <option>25</option>
                        <option>26</option>
                        <option>27</option>
                        <option>28</option>
                        <option>29</option>
                        <option>30</option>
                    </select>
                </p>
            <input type = "submit" name = "button" value = "Change Stats" class = "HoverColor Button">
            
            </form>
        '''


#print styleSheet



if len(formResults) == 0:
    print '''<!DOCTYPE = html>
            <html>
                <head>
                    <title> Stat Change  </title>
                </head>
                <body>
                    <center> <h1> Change your Stats! </h1> <center>
                    <h2> You are given a total of 30 stats points to distribute. If you go over 30 points, your character will not be created. However, going less than 30 is acceptable</h2>
                    <center> <table border = 1>
                        <tr>
                            <th> HP </th>
                            <th> Mana </th>
                            <th> Armor </th>
                        </tr>
                        <tr>
                            <td> Increases the amount of hit points you have. <br>
                                The more HP you have, the more htis you can take.</td>
                            <td> Increases the amount of mana you have. <br>
                                The more mana you have, the more spells you can cast.  </td>
                            <td> Armor lessens some of the damage you take.</td>
                        </tr>
                    </table> </center>
                </body>
                        
        '''
    print forms
#print len(formResults)
if (len(formResults) > 0) and ((int(formResults["HP"].value) +  int(formResults["Mana"].value) + int(formResults["Armor"].value)) > 30):
    print '''
    <html>
        <center>
            <h1> Your Character has not been created due to having more than 30 stat points in total. <br>
            Please press to go back</h1>
            <form action = "statChange.py">
                <input type = "submit" class = "HoverColor Button" value = "Back">
            </form>
        </cener>
    </html>
    '''

elif len(formResults) > 0:
    f.write(formResults.getvalue("HP") + ',' + formResults.getvalue("Mana") + ',' + formResults.getvalue("Armor") + ',0,0\n')
    f3.write(formResults.getvalue("HP") + ',' + formResults.getvalue("Mana") + ',' + formResults.getvalue("Armor"))
    print '''<!Doctype = html>
            <html>
                <form action="intro.py">
                    <center> <input class ="HoverColor Button" type = "submit" value ="Enter the World"> </center>
                </form>
            </html>
            '''
print '''</body>
        </html>'''
f.close()
f3.close()
