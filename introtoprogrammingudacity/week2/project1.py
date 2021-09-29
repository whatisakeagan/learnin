###### STATIC VALUES/PARAGRAPHS/BLANKS ######
# Listing of the blank spaces so they can be defined for replacement
blanks = ["___1___"]

### PARAGRAPHS/PROMPTS
p1 = "TEST PARA ___1___ NUMBER ONE"
p2 = "TEST PARA ___1___ NUMBER ONE"
p3 = "TEST PARA ___1___ NUMBER ONE"

### ANSWERS
easy_answers = ["testeasy"]
med_answers = ["testmedium"]
hard_answers = ["testhard"]

###### DYNAMIC STUFF ######
### CHOOSE DIFFICULTY
## This asks the player to define the difficulty level they prefer, or kicks
## out an error message if they enter an inaccurate option 
def difficulty():
	diff_input = raw_input("Type easy, medium, or hard to select your difficulty!  ")
	if diff_input == "easy":
		diff=1
		para=p1
		answers = easy_answers
		attempt_index = 5
		return "You chose 'easy'--this means you'll have 5 attempts at each answer :)"
	elif diff_input == "medium":
		diff=2
		para=p2
		answers = med_answers
		attempt_index = 3
		return "You chose 'medium'--this means you'll have 3 attempts at each answer :)"
	elif diff_input == "hard":
		diff=3
		para=p3
		answers = hard_answers
		attempt_index = 1
		return "You chose 'hard'--this means you'll have 1 attempt at each answer :)"
	else:
		return "You must choose a difficulty level to continue!"
print difficulty()

### Process everything by crawling across the string and checking inputs against
### correct answers. If incorrect, let them try again based on difficult. If all
### attempts exhausted, kick out an error/failure message.
def blank_cutter(crawler):
	if crawler == "___1___":
		answer1 = raw_input(" ")
		if answer1 == answers:
			return "Correct! Onto the next blank space."
		else:
			attempt_index = attempt_index - 1
			if attempt_index != 0:
				return "Sorry, that's not correct! Try again."
			else :
				return "Sorry, that's not correct! You're all out of guesses and have failed the quiz :("
print blank_cutter()


def process_paragraph(para):
	processed = ''
	index = 0
	box_length = 7
	while index < len(para):
		frame = para[index:index+box_length]
		swap_out = blank_cutter(frame)
		processed += swap_out
		if len(swap_out) == 1:
			index += 1
		else:
			index += 7
	return processed
print process_paragraph(para)

def final_product():
	print difficulty()
	print process_paragraph()


#def mainf(bn,):
#	replaced =[]
#	i=pos[0:6]
#	if i = bn:

#def grading(answer):
#	if diff == 


### PUT IT ALL TOGETHER
#def fitb():
