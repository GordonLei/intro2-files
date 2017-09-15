#!/usr/bin/python
print "content-type: text/html\n"

import cgitb
cgitb.enable()

import ButtonSheet
import displayPage




print '''
        <center> <p>Your are a lone knight in a ravine <br>
                For many days and night, you hiked for miles in order to kill the final boss of this dank game. <br>
                To your horror, you see a split in the path. Do you go go to the elft path or the right apth?
                </p>
        
        <form action = "left.py">
            <input type = "submit" class = "HoverColor Button" value = "Left">
        </form>
        <form action = "right.py">
            <input type = "submit" class = "HoverColor Button" value = "Right">
        </form>

        </center>
        '''
