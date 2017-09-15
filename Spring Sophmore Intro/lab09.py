#!/usr/bin/python
print "content-type: text/html\n"

#Lei,Gordon
#Intro2,pd.1
#Lab09
#2016-04-11

#NOTES:
# ;=; y for loops not stronk enuff for this part.
# It will be pretty cool to just use for loops to check individual words
#    and ignore puncutations by using splices (like word[0:4] to check only for
#    'NOUN' but it can include 'NOUN,') & split() & ' '.join........
#    Problem is, doign something like
#            for word in storyString.split():
#               word = word.replace(word[0:4], randomWord(nouns)
#    won't actually change the word but just make the variable "word" become
#    the new word. If u try looking for list indexes for "NOUN", it won't count
#    suff like "NOUN?" but if you strip punctuation, you have to add them back
#   somehow
#   So I just did some cheesy
#      while "NOUN" in storyString loops. 



import random
#use this for testing purposes, theme your website later.

def randomWord(L):
    return L[random.randint(0,len(L) - 1)]

nouns=['fish','computer','Iphone','jaguar','mapo tofu']
verbs=['run','spin','talk','hit','jig','shave','cut','rap']
adjectives=['silent','big','small','hairy','rich','amazing','outrageous','preposterous']

#Hamlet ='''To be, or not to be--that is the question:
#Whether 'tis nobler in the mind to suffer
#The slings and arrows of outrageous fortune
#Or to take arms against a sea of troubles
#And by opposing end them. To die, to sleep--
#No more--and by a sleep to say we end
#The heartache, and the thousand natural shocks
#That flesh is heir to. '''

Hamlet ='''To VERB, or not to VERB--that is the NOUN:
Whether 'tis nobler in the NOUN to VERB
The NOUNs and NOUNs of ADJECTIVE fortune
Or to take NOUNs against a sea of NOUNs
And by opposing end them. To VERB, to VERB--
No more--and by a VERB to say we end
The heartache, and the thousand ADJECTIVE VERB
That flesh is heir to. '''

#Hachiman =''' Animals naturally form packs. 
#Carnivores form social hierarchies within their packs.
#Those that fail to become alphas harbor the burden of failure until they die.
#I'm sure the herbivores feel guilt as they sacrifice their comrades to evade their predators and live on.
#In this world, forming packs yields no benefit for the individual.
#Thus, I choose the way of the solitary bear, which does not form packs.
#The bear finds no anxiety in living alone.
#He is proud.
#He is a lone wolf.
#Furthermore, they hibernate in the winter.
#How wonderful that must be.
#There is no doubt in my mind.
#In my next life, I want to be a bear. '''

Hachiman ='''NOUNs naturally form NoUN1s. 
NOUN form ADJECTIVE NOUNs within their NoUN1s.
Those that VERB to become NOUNs harbor the burden of failure until they die.
I'm sure the NOUNs feel guilt as they sacrifice their comrades to evade their NOUNs and live on.
In this world, forming NoUN1s yields no benefit for the individual.
Thus, I choose the way of the ADJECTIVE NoUN2, which does not form NoUN1s.
The NoUN2 finds no NOUN in living alone.
He is ADJECTIVE.
He is a lone wolf.
Furthermore, they VERB in the NOUN.
How wonderful that must be.
There is no doubt in my mind.
In my next life, I want to be a NoUN2. '''

def textSelector():
    text = ''
    number = random.randint(1,2)
    if number == 1:
        text = Hamlet
    if number == 2:
        text = Hachiman
    return text

storyString = textSelector()
    
def madLib(storyString, nouns, verbs, adjectives):
    noun1 = randomWord(nouns)
    noun2 = randomWord (nouns)
    nouns.remove(noun1)
    nouns.remove(noun2)
    while "NOUN" in storyString: #these while loops will always change 1 part of speech at a time
        storyString = storyString.replace("NOUN", randomWord(nouns),1)
    while "NoUN1" in storyString:
        storyString = storyString.replace("NoUN1", noun1)
    while "NoUN2" in storyString:
        storyString = storyString.replace("NoUN2", noun2)
    while "VERB" in storyString:
        storyString = storyString.replace("VERB", randomWord(verbs),1)
    while "ADJECTIVE" in storyString:
        storyString = storyString.replace("ADJECTIVE", randomWord(adjectives),1)
    return storyString



def startPage():
    htmlTags = "<html> \n <head> \n <title> " + "Title" + "</title> \n </head> \n <body>"
    return htmlTags


def endPage():
    htmlTags = "</body> \n </html>"
    return htmlTags
            
print startPage()
print "<p>" + madLib(storyString, nouns, verbs, adjectives) + "</p>"
print endPage()
