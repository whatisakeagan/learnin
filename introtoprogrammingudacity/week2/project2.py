###### DEFINE QUESTIONS AND ANSWERS
blanks = ["___1___", "___2___", "___3___", "___4___", "___5___"]

easyQs = "Despite any media that says otherwise, ___1___ aren't related to autism in any meaningful way. Many people think that being ___2___ brained means you're more ___3___, but there's no meaningful distinction in personality based on which half of the brain you might use more. Additionally, healthy individuals do not use one ___4___ of their brain more than the other. The truth is that everyone is more likely to be affected by life ___5___ than anything else, and that will affect a person's behavior most of all."
easyAs = ["vaccines", "right", "creative", "half", "experiences"]

medQs = "People seem to think that ___1___ makes your memory of an experience stronger. People often call these ___2___ moments. However, there's actually little evidence to support that; in reality, people's memory is less than perfect, even when it comes to very salient experiences such as 9/11. The sense that creates the strongest memories is actually one's sense of ___3___. These are called ___4___ memories. As with most memories, they're processed by the brain's ___5___."
medAs = ["emotion", "lightbulb", "smell", "olfactory", "hippocampus"]

hardQs = "___1___ is credited as being the 'Father of Psychology,' but most of his theories have been debunked. Similarly, though ___2___ created the ubiquitous ___3___ personality test, results of that test are not really meaningful in any significant way. A much more accurate test is the ___4___, created by the University of ___5___."
hardAs = ["Freud", "Jung", "Myers-Briggs", "MMPI", "Minnesota"]

###### EVERYTHING BELOW DEFINES FUNCTIONS FOR THE ENTIRE QUIZ
### FUNCTION TO DETERMINE QUESTION SET
def qdiff(diff_input):
	if diff_input == "easy":	
		return easyQs
	elif diff_input == "medium":
		return medQs
	elif diff_input == "hard":
		return hardQs
	else:
		return "You must choose a difficulty level to continue! Please restart the program."

### FUNCTION TO DETERMINE ANSWER SET
def adiff(diff_input):
	if diff_input == "easy":
		return easyAs
	elif diff_input == "medium":
		return medAs
	elif diff_input == "hard":
		return hardAs

### FUNCTION TO DETERMINE ATTEMPTS ALLOWED
def att_allowed(diff_input):
	if diff_input == "easy":
		return 5
	elif diff_input == "medium":
		return 3
	elif diff_input == "hard":
		return 1

## FUNCTION TO TELL USER THE RULES
def rules(diff_input):
	if diff_input == "easy":
		return "You chose 'easy' -- this means you'll have 5 attempts on the entire quiz, and your questions will be of little difficulty."
	elif diff_input == "medium":
		return "You chose 'medium' -- this means you'll have 3 attempts on the entire quiz, and your questions will be of moderate difficulty."
	elif diff_input == "hard":
		return "You chose 'hard' -- this means you'll have 1 attempt on the entire quiz, and your questions will be of significant difficulty."

###### FULL QUIZ--PUT IT ALL TOGETHER
def psyc_quiz():
	# Ask user for which difficulty they want
	difficulty = raw_input("You'll be taking a quiz about debunking common psychology myths--you'll have to fill in 5 different blanks. Type easy, medium, or hard to select your difficulty! ")
	# Tells the user how many attempts they'll have based on what they chose
	print rules(difficulty)
	# Shows the user the quiz content with blanks
	print qdiff(difficulty)
	index = 0
	# Dynamically defines max attempts allowed based on difficulty
	attempts = att_allowed(difficulty)
	while index < len(blanks):
		# Locally defines difficulty so the quiz can progress through the blanks
		user_pref = qdiff(difficulty)
		# Asks the user for an answer to whatever blank is current based on the index
		response = raw_input(blanks[index] + "should be replaced with what word? ")
		# If the user is correct, tell them that, and move onto the next blank using the index
		if response == adiff(difficulty)[index]:
			print ("Correct! Onto the next one!")
			index += 1
			# If the user is at the end AND they get it correct, congratulate them
			if index == 5:
				print ("Great work! You're all done now--be sure to show up the rest of your friends who think they know stuff but don't!")
		# If they're not correct, check how many attempts are left
		# If they have attempts left, subtract one attempt for being wrong,
		# tell them how many attempts they have left, and loop back to where they're stuck.
		elif attempts > 1:
			attempts = attempts - 1
			satt = str(attempts)
			print ("Nope! Try again. You have " + satt + " attempts left.")
		# If they're not correct, and they have no attempts left, end the quiz
		else:
			index = len(blanks)
			print "Sorry--you're all out of attempts! Restart the program to try again."

psyc_quiz()
