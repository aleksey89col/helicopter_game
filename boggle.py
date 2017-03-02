#!/usr/bin/env python
# Helmut Cardenas FSUID = hac14d
import random
import enchant
import __future__


# pass a string and returns a single character from string
def guess_letter(str):
    return random.choice(str)


# determines ammount of point that the 
# winning word wins 
def calc_points(word) :
	length = len(word)
	if length == 3 or length == 4:
		return 1
	if length == 5 :
		return 2
	if length == 6 :
		return 3
	if length == 7 :
		return 5
	if length >= 8 :
		return 11

# checks if the word is in the given list
# it does by checking if every character is present 
# in the 16 randon character list 
def is_present(word, list_of_char) :
	char_word_list = list(word)
	for char in char_word_list :
		if char not in list_of_char :
			return False

	return True

# main function of boogle
def play_boogle() :

	# these are the 16 die
	alpha = ["AEANEG","AHSPCO", "ASPFFK", "OBJOAB", 
	"IOTMUC", "RYVDEL", "LREIXD", "EIUNES", "WNGEEH",
	"LNHNRZ", "TSTIYD", "OWTOAT", "ERTTYL", "TOESSI", 
	"TERWHV", "NUIHMQu"]

	# initialize the list of letters
	list_random_letters = []
	for x in alpha:
		list_random_letters.append(guess_letter(x))

	#since the last die has a character that counts for 2 
	# it checks if the random function returned Q or u and makes it into Qu
	if list_random_letters[-1] == 'Q' or list_random_letters[-1] == 'u' :
		list_random_letters[-1] = 'Qu'


	# simple print of the board 
	for x in range(0,16) :
		if x % 4 == 0 :
			print()
		else :
			print("[",list_random_letters[x], "] ", end='')

	print("\nStart typing your words!\n(press enter after each word and enter'X' when done):")

	# gets player input and stores it into a list
	player_input = ""
	player_input_list = []
	while player_input  != "X"  :
		player_input = input(">").upper().strip()
		player_input_list.append(player_input)

	# removes the exiting character
	player_input_list.remove("X")


	#  setting variables for game logic
	dic = enchant.Dict("en_US")
	final_score = 0
	word_set = []

	# game logic is as follows
	# if we havent seen the word continue checking otherwise print has already been used
	# if playes input is actual word continue checking otherwise print not a word
	# if the word is len is greater than 3 continue checking otherwise print too short
	# if the word can be made with character from die the word is good update score 
	for word in player_input_list :
		if word not in word_set:
			word_set.append(word)

			if dic.check(word) :
				if len(word) >= 3 :
					if is_present(word, list_random_letters) :
						word_score = calc_points(word)
						print("The word ", word, " is worth ", word_score , "points.")
						final_score += word_score
					else : 
						print("The word ", word, " is not present.")
				else :
					print("The word ", word, " is too short.")
			else  :
				print("The word ", word, " is ... not a word.")
		else :
			print("The word ", word, " has already been used.")
			

	print("Your total score is ", final_score , " points!")




if __name__ == '__main__':
	play_boogle()