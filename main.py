import flask
import random
import re


def getRandomLine(rsv):                 # GetRandomLine code created by David. Those comments were his.
    file_h = open(rsv)                  #a file handle for the .txt in question
    limit = file_h.readline()           #the number of lines to search per the .txt
    limit = limit.replace('\n', '' )    #trim the return character
    limit = int(limit)                  #the number literal converted to int
    line = random.randint(0, limit - 1) #which line to search
    
    for x in range(line):
        file_h.readline()               #parse through that shit until search reached
    phrase = file_h.readline()          #if you gotta big d*** lemme search it. 
    phrase = phrase.replace('\n', '')   #get rid of trailing returns cause those are gross
    
    return(phrase)

	
def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def main(leg):

	poke = ""

	if leg == "yes":
		poke = getRandomLine('allPoke.txt')
	else:
		poke = getRandomLine('allPokeNoLeg.txt')
		
	flask.flash(poke)
	

def start(party,leg):

	partySize = 1

	if is_number(party):
		if int(party) > 6:
			partySize = 6
		else:
			partySize = int(party)
		
		for i in range(partySize):
			main(leg)
	else:
		main(leg)

