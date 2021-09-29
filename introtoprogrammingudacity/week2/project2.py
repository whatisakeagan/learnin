###### DEFINE QUESTIONS AND ANSWERS
blanks = ["___1___", "___2___", "___3___", "___4___", "___5___"]

easyQs = "Despite any media that says otherwise, ___1___ aren't related to autism in any meaningful way. Many people think that being ___2___ brained means you're more ___3___, but there's no meaningful distinction in personality based on which half of the brain you might use more. Additionally, healthy individuals do not use one ___4___ of their brain more than the other. The truth is that everyone is more likely to be affected by life ___5___ than anything else, and that will affect a person's behavior most of all."
easyAs = ["vaccines", "right", "creative", "half", "experiences"]
easyatt = 5
easyind = 0

medQs = "People seem to think that ___1___ makes your memory of an experience stronger. People often call these ___2___ moments. However, there's actually little evidence to support that; in reality, people's memory is less than perfect, even when it comes to very salient experiences such as 9/11. The sense that creates the strongest memories is actually one's sense of ___3___. These are called ___4___ memories. As with most memories, they're processed by the brain's ___5___."
medAs = ["emotion", "lightbulb", "smell", "olfactory", "hippocampus"]
medatt = 3
medind = 0

hardQs = "___1___ is credited as being the 'Father of Psychology,' but most of his theories have been debunked. Similarly, though ___2___ created the ubiquitous ___3___ personality test, results of that test are not really meaningful in any significant way. A much more accurate test is the ___4___, created by the University of ___5___."
hardAs = ["Freud", "Jung", "Myers-Briggs", "MMPI", "Minnesota"]
hardatt = 1
hardind = 0

###### EVERYTHING BELOW DEFINES FUNCTIONS FOR THE ENTIRE QUIZ
### DETERMINE QUIZ PARAMETERS BASED UPON DIFFICULTY SELECTION
## Accepts difficulty input from user
## Returns values corresponding to question, answer sets and attempts allowed
## Prints information about difficulty level
def udiff(diff_input):
	if diff_input == "easy":
		print "You chose 'easy' -- this means you'll have 5 attempts on the entire quiz, and your questions will be of little difficulty."
		return easyQs, easyAs, easyatt, easyind
	elif diff_input == "medium":
		print "You chose 'medium' -- this means you'll have 3 attempts on the entire quiz, and your questions will be of moderate difficulty."
		return medQs, medAs, medatt, medind
	elif diff_input == "hard":
		print "You chose 'hard' -- this means you'll have 1 attempt on the entire quiz, and your questions will be of significant difficulty."
		return hardQs, hardAs, hardatt, hardind

###### FULL QUIZ--PUT IT ALL TOGETHER
## Processes raw input from user for difficulty
## Prints out progressively answered paragraph for correct answers
## Prints a message indicating incorrect answers where applicable, along with a prompt indicating how many attempts left
## Prints a message when finished--both successfuly and unsuccessfully
def psyc_quiz():
	# Ask user for which difficulty they want
	difficulty = raw_input("You'll be taking a quiz about debunking common psychology myths--you'll have to fill in 5 different blanks. Type easy, medium, or hard to select your difficulty! ")
	selectQ, selectA, attempts, index = udiff(difficulty)
	# Shows the user the quiz content with blanks
	print selectQ
	# Locally defines difficulty so the quiz can progress through the blanks
	while index < len(blanks):
		# Asks the user for an answer to whatever blank is current based on the index
		response = raw_input(blanks[index] + "should be replaced with what word? ")
		if response == selectA[index]:
			print ("Correct! " + str(selectQ.replace(blanks[index], response)+ " Onto the next one!"))
			selectQ = selectQ.replace(blanks[index], response)
			index += 1
			# If the user is at the end AND they get it correct, congratulate them
			if index == len(blanks):
				print ("Great work! You're all done now--be sure to show up the rest of your friends who think they know stuff but don't!")
		# If they're not correct, check how many attempts are left
		# If they have attempts left, subtract one attempt for being wrong,
		# tell them how many attempts they have left, and loop back to where they're stuck.
		elif attempts > 1:
			attempts = attempts - 1
			print ("Nope! Try again. You have "+str(attempts)+" attempts left.")
		# If they're not correct, and they have no attempts left, end the quiz
		else:
			index = len(blanks)
			print "Sorry--you're all out of attempts! Restart the program to try again."
psyc_quiz()
