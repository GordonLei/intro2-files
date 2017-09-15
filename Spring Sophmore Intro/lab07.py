#!/usr/bin/python
print "content-type: text/html\n"

#Lei,Gordon
#Intro2, pd1
#Lab07
#2016-03-18


#to help debug
import cgitb
cgitb.enable()

#needed this
def hasNumber(s):
    return False
    for c in "0123456789":
        if c in s:
            return True;
    return False;

#process a url appliying your function to each word
def modifySite(url,f):
    #to get info from the URL string
    import cgi
    form = cgi.FieldStorage()
    if "url" in form:
        url = form.getvalue('url')
    #to load a web page into a string
    import urllib2
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    page = response.read()
    #to get the root of the website this is a hacky way for valid urls..
    if("://" in url):
        url = url[:url.find("/",8)+1]
    else:
        url = url[:url.find("/")+1]

    #in case not a valid html page:
    head = "<html><head><title>Random Page?</title></head>\n<body>"
    if "<body" in page:
        head = page.split("<body")[0]
        page = page.split("<body")[1]
        page = "<body>\n"+page[page.find(">")+1:]

    #This is just a quick and dirty solution
    #that will fix SOME broken links and css. (Works on wikis)
    head = head.replace('src="','href="'+url)
    page = page.replace('src="','href="'+url)
    head = head.replace(url+'/',url)
    page = page.replace(url+'/',url)
    head = head.replace('href="/','href="'+url)
    page = page.replace('href="/','href="'+url)
   
    #process the words not in tags.
    tag = False;
    quote = False;
    last =''
    ans = ""
    index = 0;
    start = 0;
    end = 0;
    justended = False;
    line = []
    for c in page:
        if c == "<" and not quote:
            tag = True
            end = index
            justended = True;
        elif c == ">" and not quote:
            tag = False
            ans+=c
            start = index+1
        elif not tag and c =='"':
            quote = not quote
        if tag:
            if(justended):
                justended=False;
                line = page[start:end]
                words = line.split();
                for word in words:
                    prefix =""
                    suffix =""
                    #check for punctuation!
                    if len(word) > 0 and not word[0].isalpha():
                        prefix = word[0]
                        word = word[1:]
                    if len(word) > 0 and not word[-1].isalpha():
                        suffix = word[-1]
                        word = word[:-1]
                    if not hasNumber(word):
                        if len(word) > 0 and word[0]>='A' and word[0]<='Z':
                            word = f(word).capitalize()
                        else:
                            word = f(word)
                    ans+= prefix + word +suffix+" "
            ans+=c
        index += 1
    return head + ans

######################################################
#PLACE YOUR FUNCTIONS HERE:

#pigLatin
def pigLatin(c):
    word = str(c)
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    ending = ""
    #Empty strings are considered to be false. 
    if (c == False) or (c == ""):
        return ""
    elif ((word[0] in vowels) == True):
        word = word + "hay"
        return word
    else:
        while (len(word) > 0) and not(word[0] in vowels):
            ending = ending + word[0]
            word = word[1:len(word)]
        word = word + ending + "ay"
        return word
    
#rot13
def rot13char(c):
    if (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z'):
        if (c >= 'a' and c < 'n') or (c >= 'A' and c < 'N'):
            return chr(ord(c) + 13)
        else:
            return chr(ord(c) - 13)
    else:
        return c

def rot13(string):
    n = 0
    rot13str = ''
    while n < len(string):
        rot13str = rot13str + rot13char(string[n])
        n = n + 1
    return rot13str
#romanize
def romanize(s):
    s = s.replace("U","V")
    s = s.replace("u","v")
    return s
#no change
def noChange(s):
    return s
#make silly changes
def addIsh(s):
    return s+"ishkabibble"

#modifyWords
import random

def modifyWords(s):
    number = random.randint(0,99)
    if number >= 0 and number < 33:
        return pigLatin(s)
    if number >= 33 and number < 66:
        return rot13(s)
    if number >= 66 and number <= 99:
        return pigLatin( rot13 (s))






url ='https://en.wikipedia.org/wiki/Latin'
######################################################
#which function to use? (notice do not CALL the function, just give the function name!)
function = modifyWords
#Replace noChange to whichever function you would like to be applied to the website:
#e.g.
#function = addIsh
#or
#function = romanize

#this uses 
print modifySite(url,function)
