print '''<style type = "text/css">
.title {text-align:center;
        color: violet;}
.button {width: 140px;
        height: 40px;
        font: bold 11px Arial;
        text-decoration: none;
        background-color: #EEEEEE;
        color: #333333;
        padding: 2px 6px 2px 6px;
        border-top: 1px solid #CCCCCC;
        border-right: 1px solid #333333;
        border-bottom: 1px solid #333333;
        border-left: 1px solid #CCCCCC;}
.buttonHover:hover {background-color:33CCFF;}
.center {text-align:center;}
        div.translucentBox {background: rgba(204,204,204,0.4);
        width: 33%;
        height: 25%;
        text-align:center;}

.ToastBackground {
        background-image: url("../images/toast2.jpg");
        background-attachment: fixed;
        background-size: 100% 100%;}

.baguette {background-image: url("../images/baguette.jpg");}

.BreadPost {
    background-color: #c68958;
    padding: 30px;
    border-radius: 50px;
    margin: 5px;}
.ButterComment {
    background-color: #ffff91;
    border-radius: 10px;
    padding: 10px;
    margin: 5px;
}

input[type=text]:focus {background-color: cyan;
        border: 4px solid #555;
        color: red;}
input[type=password]:focus {background-color: cyan;
        border: 4px solid #555;
        color: red;}
input[type=textfield]:focus {background-color: cyan;
        border: 4px solid #555;
        color: red;}
textarea:focus {background-color: cyan;
        border: 4px solid #555;
        color: red;}
input[type=submit] {width: 140px;
        height: 40px;
        font: bold 11px Arial;
        text-decoration: none;
        background-color: #EEEEEE;
        color: #333333;
        padding: 2px 6px 2px 6px;
        border-top: 1px solid #CCCCCC;
        border-right: 1px solid #333333;
        border-bottom: 1px solid #333333;
        border-left: 1px solid #CCCCCC;}
input[type=submit]:hover {background-color:33CCFF;}


.color {background-color:orange;}
.color2 {background-color:#2cc48a;}
ul{list-style-type: none;
        background-color: #333;
        overflow: hidden;}
li{float:left;
        border-right:1px solid #bbb;}
li a{display:block;
        color: white;
        text-align:center;
        padding:16px 20px;}
li a:hover {background-color:cyan}
li a:hover:not(.color) {background-color: cyan;}
        </style>'''


def displayInboxWidget(cookie):
	currentUser = cookie["username"].valu
	userDict = stdStuff.objFileToList(stdStuff.directory,
								stdStuff.userFile, byName=True)
	
	res = \
"""
<div align='right'>
	<table border='1'>
		<tr>
			<td>
				<a href="inbox.py">View messages</a>
			</td>
		</tr>
	</table>
</div>
"""
	return res
def displayGroupWidget(cookie):
	currentUser = cookie["username"].value
	userDict = stdStuff.objFileToList(stdStuff.directory,
								stdStuff.userFile, byName=True)
	
	res = \
"""
<div align='right'>
	<table border='1'>
		<tr>
			<td>
				<a href="groups.py">View groups</a>
			</td>
		</tr><
	</table>
</div>
"""
	return res



