#Creating 3 different quiz scenarios with blanks and giving definitions 
#for each scenario with containing Lists.
easy_quiz='''___1___ is a method that can help you to find the target in 
the string. ___2___ is a method that can help you to find out the 
quantity of items of the string. ___3___ is a command to show the type of the command. 
___4___ is a helper command to find out help info of the command'''
easy_answers=["find", "len", "type", "help"]
easy_blanks=["___1___", "___2___", "___3___", "___4___"]
easy=[easy_quiz, easy_answers, easy_blanks]

medium_quiz='''In the terminal ___1___ command shows the content of directory, 
to change to a different directory enter ___2___ command, to create new directory
enter ___3___ command and to remove a file use ___4___ command'''
medium_answers=["ls", "cd", "mkdir", "rm"]
medium_blanks=["___1___", "___2___", "___3___", "___4___"]
medium=[medium_quiz, medium_answers, medium_blanks]

hard_quiz='''dictionary={"easy":easy, "medium":medium, "hard":hard}
In this dictionary [("easy":easy),("medium":medium),("hard":hard)] are called ___1___, 
["easy", "medium", "hard"] are called ___2___ ,[easy, medium, hard] are called ___3___ 
and [easy, medium, hard] all together is a ___4___'''
hard_answers=["items", "keys", "values", "list"]
hard_blanks=["___1___", "___2___", "___3___", "___4___"]
hard=[hard_quiz, hard_answers, hard_blanks]

#Creating Dictionary to combine all scenarios with coresponding Values.
dictionary={"easy":easy, "medium":medium, "hard":hard}
#Per my reviewer creating these Global Variables to avoid using Magic Numbers
index_quiz=0 
index_results=1 
index_blanks=2

def welcome():
	#Per reviewer's suggestion had to brake single long function in to 3 functions 
	#in order to meet the requirement no more then 18 lines.
	#To make it more fun I've personalized the begining of the game.
	#this function to output the player's name per the raw_input.
	#Anyway since my functions multiplied I have to complete the function
	#with return, which made my player's name not global for following functions.
	print 80*"-"+"\n"+"Hello! What's your name?"
	player=raw_input()
	#global player
	#Lack of my knowledge on relativity of Global and Local
	#variables, I found the command global to make the player's name carried 
	#across next functions. (see line 42).
	#I would apreciate some inputs on variables.
	print "    Hi "+player+", please choose difficulty level: Easy, Medium or Hard"
	return player
def select_difficulty(player):
	#This function will output the result of the difficulty level.
	attempts=4
	difficulty=raw_input().lower()
	#Anyway I had made a While Loop in the previous single function to interrupt 
	#the game, since my kids were always playing not by the rules, lol, and 
	#making it fail consistantly choosing incorrect dificulty level.
	#And again multiple functoins made my job interestingly chalenging, since
	#after 4 unsuccessful attempts the writing "wow..." would become as output 
	#of my function and as input for the function 'quiz'. (see line 66)
	#The code will work as required anyway, but again, I'd apreciate some inputs
	#for me to get better at understanding multiple functions.
	while difficulty not in dictionary.keys():
		print "Please try to choose one of these options: Easy, Medium or Hard"
		difficulty=raw_input().lower()
		attempts-=1
		if attempts<1:
			print "WOW!!! "+player+" You failed to choose difficulty level??? GAME OVER!!!"
			exit() 
	level=dictionary[difficulty]
	print '      Level-"'+difficulty+'".    You have 5 attempts.'
	#thanks for the tip on *'-' and '\n'
	print 80*"-"+"\n"+level[index_quiz]+"\n"
	return level
def quiz(level, player):
	#This is the final function, that will use the results of previous functions as input and
	#will output results.
	attempts=5
	question=level[index_quiz]
	#the method 'zip' is making it easy to eliminate nested loops.
	for results,blank in zip(level[index_results], level[index_blanks]):
		answer=raw_input(80*"-"+"\n"+player+"! What's your answer for "+ blank+" ?    ").lower()
		#creating while loop to check if the answer matches to results and take 1 attempt 
		#after each wrong answer and end the game after 5 wrong attempts.
		while answer!=results:
			print "That's not correct. Please try again."
			print "---You have "+str(attempts-1)+" attempt(s)---"
			answer=raw_input().lower()
			attempts-=1
			if attempts==1:
				return "That's not correct. GAME OVER!"
		#using replace method to replace blanks and answers 
		#after which print the updated version of "level"
		question=question.replace(blank,answer)
		print 80*"-"+"\n"+"Correct!!! "+"\n"+question
	return 80*"-"+"\n"+"Winner  "+player+"!!!"
#print quiz(select_difficulty(welcome())
variable_player=welcome()
variable_level=select_difficulty(variable_player)
print quiz(variable_level, variable_player)