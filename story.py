import time
from faces import story_faces as sf

line_1 = "Hi! I am Breadman."
line_2 = "I have been accused for stealing bread."
line_3 = "But, I am innocent."
line_4 = "They say, I will not be hanged till death if I play a game called Hangman."
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


def now_the_game():
    print("\n1: Start\n2: Rules")

    rules_or_start = input("\nChoose your option: ")

    if rules_or_start == "2":
        print()
        print("Randomly, a word will be printed on the screen, with only one letter of it shown to you.")
        time.sleep(5)
        print("You will have to guess what might be the letters in that word, one by one.")
        time.sleep(5)
        print("You have 5 attempts until Breadman dies.")
        time.sleep(3)
        print("Good luck!")
        time.sleep(2)
        input("\nPress Enter to go back to the two-option menu.")
        now_the_game()
    elif rules_or_start != "1":
        print("\nInvalid option.")
        now_the_game()
    else:
        pass


def the_end():
    good_bye = "Thank You for playing this game!"
    the_end = "Breadman, signing out!"
    print()
    for x in good_bye:
        print(x, end = "")
        time.sleep(0.1)
    print()
    print()
    time.sleep(0.5)
    print(sf[1])
    time.sleep(0.5)
    for x in the_end:
        print(x, end = "")
        time.sleep(0.1)
