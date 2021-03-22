import time
from faces import story_faces as sf

line_1 = "Hi! I am Breadman."
line_2 = "I have been accused for stealing bread."
line_3 = "But, I am innocent."
line_4 = "They say, i will not be hanged till death if i play a game called Hangman."
line_5 = "Now, you, and only you, can save me, your Breadman, from getting hanged."

def story():
	print()
	for x in line_1:
		print(x, end = "")
		time.sleep(0.1)
	print()
	print(sf[1])

	input("Press Enter to continue.")

	print()
	for x in line_2:
		print(x, end = "")
		time.sleep(0.1)
	print()
	time.sleep(1)
	for x in line_3:
		print(x, end = "")
		time.sleep(0.1)
	print()
	print(sf[2])

	input("Press Enter to continue.")

	print()
	for x in line_4:
		print(x, end = "")
		time.sleep(0.1)
	print()
	time.sleep(1)
	for x in line_5:
		print(x, end = "")
		time.sleep(0.1)
	print()
	print(sf[2])

	input("Press Enter to continue.")

def rules_or_start():
	print("\n1: Start\n2: Rules")

	lets_begin = input("\nSelect your option: ")
	if int(lets_begin) == 2:
		print("\nRandomly, a word will be printed on your screen, in which only one letter will be shown to you that's in that word.")
		time.sleep(5)
		print("You'll have 5 attempts to guess the word correctly.")
		time.sleep(5)
		print("If all your attempts are over and you don't guess the word correctly, Breadman dies.")
		time.sleep(5)
		print("Good luck!")
		time.sleep(1)
		rules_or_start()
	elif int(lets_begin) != 1:
		print("\nInvalid option.")
		rules_or_start()
	else:
		pass
