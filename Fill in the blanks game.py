
# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!

# To help you get started, we've provided a sample paragraph that you can use when testing your code.
# Your game should consist of 3 or more levels, so you should add your own paragraphs as well!


# first we define the functions necessary for the code to run.

def introduction():
	'''
	Behaviour: Asks the user to pick a level in the game
	Input: None
	Output: Level the user chooses
	'''
	level_chosen = ''
	levels = ['easy', 'medium', 'hard']

	while level_chosen not in levels:
		print('Please select a game difficulty by typing it in!')
		print('Possible choices include easy, medium and hard')
		level_chosen = input()
		level_chosen = level_chosen.lower()
		if level_chosen not in levels:
			print("That's not an option!")
	else:
		return level_chosen


def isSubstituted(paragraph):
	'''
	Behaviour: Checks if all word have been replaced in the string
	Input: A paragragh
	Output: True or False depending on the strings
	'''
	if '__' in paragraph:
			return False
	return True


def toSubstitute(replacement, space, paragraph):
	'''
	Behaviour: Substitutes the blanks in the paragraph with the user's input
	Input: User's guess, the blank to be substituted and the paragraph
	Output: paragraph without the blank
	'''
	assert '__' in space
	if space in paragraph:
		return paragraph.replace(space, replacement)


def identifySubstitute(paragraph):
	'''
	Behaviour: Locates the next blank space
	Input: Paragraph
	Output: The blank space as represented
	'''
	index = paragraph.index('___')
	substitute_length = 7
	return paragraph[index: index + substitute_length]


def game(level_chosen, paragraph, answers):
	'''
	Behaviour: Runs the game for the player.
	Input: The level chosen, the paragraph based on the level choosen, and the list of answers.
	Output: None
	'''
	guesses, user_input, substitute_paragraph, index = 5, '', paragraph[:], 0
	print('You have chosen ' + level_chosen + '!' + '\n  ' + '\nYou will get ' + str(guesses) + ' guesses per problem' + '\n ')
	
	while not isSubstituted(paragraph):
		substitute_word, last_guess = identifySubstitute(paragraph), 1
		print('The current paragraph reads as such:' + '\n' + substitute_paragraph + '\n' )
		user_input = (input('What should be substituted in for ' + substitute_word + '? ')).lower()
		
		if user_input in answers[index]:
			print('\nCorrect!')
			substitute_paragraph, paragraph, index = toSubstitute(user_input, substitute_word, paragraph), toSubstitute(user_input, substitute_word, paragraph), index + 1
		else:
			guesses -= 1
			if guesses < last_guess:
				break
			else:
				print("\nThat's not the correct answer: Let's try again; you have {} try left".format(guesses))

	if isSubstituted(paragraph):
		print(substitute_paragraph + '\nYou won!')

# Then the games variables for the diffrent levels.


game_levels = {'easy': { 'phrase': '''A common first thing to do in a language is display
 	 'Hello ___1___!' In ___2___ this is particularly easy; all you have
 	 to do is type in: ___3___ "Hello ___1___!". Of course, that isn't a
 	very useful thing to do. However, it is an example of how to output 
 	to the user using the ___3___ command, and produces a program which 
 	does something, so it is useful in that capacity. It may seem a bit 
 	odd to do something in a Turing complete language that can be done 
 	even more easily with an ___4___ file in a browser, but it is a step
 	 in learning ___2___ and that is really it's purpose''',
 	  'answers': ('world', 'python', 'print', 'html')},
 
 'medium': {'phrase': '''A ___1___ is created with the def keyword. You specify 
 	the inputs a ___1___ takes by adding ___2___ separated by commas between
 	 the parentheses. ___1___s by default return ___3___ if you don't specify
 	 the value to return. ___2___ can be standard data types such as string,
 	 number, dictionary, tuple, and ___4___ or can be more complicated such
 	 as objects and lambda functions.''', 
 	'answers': ('function', 'arguments', 'none', 'list')},
 
 'hard': {'phrase': '''When you create a ___1___, certain ___2___ are 
 	automatically generated for you if you don't make them manually. An 
 	object is an ___3___ of a class is. Binary operators can also be 
 	created for the class e.g ___4___ which lets '+' be used on the class''', 
 	'answers': ('class', 'methods', 'instance', 'add')}}

def progress_game(level_chosen):
	'''
	Behaviour: Starts the game and sets up the paragraph and the answer for the game.
	Input: level_chosen
	Output: None
	'''
	game_level = game_levels[level_chosen]
	return game(level_chosen, game_level['phrase'], game_level['answers'])


# Initialize the game.
level_chosen = introduction()

if level_chosen != None:
    progress_game(level_chosen)