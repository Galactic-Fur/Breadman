import random
from words_with_category import word_collection as wc
from faces import faces


def print_menu():
    """Prints main menu"""
    
    print("\n------ Hangman ------")
    print("--- with Breadman ---\n")

    for i, collection in enumerate(wc.keys()):
        print("{}: {}".format(i + 1, collection))


def select_word(category_selection):
    """Selects a random word from a category"""

    random_word_string = random.choice(wc[list(wc.keys())[category_selection - 1]])
    return random_word_string


def word_with_blanks(word, right_letters_from_user):
    """Returns the word blank with filled-in letters"""

    to_be_printed_string = ""
    for letter in word:

        # the letter is guessed by the user and is in the randomly picked word
        
        if letter in right_letters_from_user:
            to_be_printed_string += letter.upper() + " "

        # the letter is not guessed by the user and is in the randomly picked word
        
        elif letter.isalnum():
            to_be_printed_string += "_ "
            
        else:
            to_be_printed_string += "  "

    return to_be_printed_string


def category_from_user():
    """Asks category from user and picks a random word from the selected category"""

    while True:
        selection = input("\nEnter your selection: ")

        if selection.isdigit() and selection in ("1", "2", "3", "4", "5", "6"):
            replaced_word = select_word(int(selection))
            return replaced_word

        # ask the user to choose a category again if he enters an invalid character

        else:
            print("That category doesn't exist!")


def input_letter_from_user(letters_guessed):
    """Takes a letter from the user as input"""

    while True:
        user_input = input("\nGuess a letter: ")

        if len(user_input) == 1 and user_input.isalpha():
            if user_input in letters_guessed:
                print("Letter", user_input.upper(), "already guessed.")
            else:
                return user_input.lower()

        # ask the user to guess a letter again if he enters an invalid character
        
        else:
            print("Please enter a valid letter.\n")
        


def print_face(attempts_left):
    """Prints faces based on attemps left"""
    
    print(faces[attempts_left])
    print("\nAttempts left: ", attempts_left)


def game_is_won(word, letters_guessed):
    """Check if the user has guessed the word correctly"""

    for letter in word:
        if (letter not in letters_guessed) and (letter.isalpha()):
            return False
    return True


def run_game(word):
    """Runs the game and does all the printing while its running"""
    
    attempts = 5

    word_with_case = word
    word = word.lower()

    # let random letter be already filled in

    letters_guessed = [random.choice(word)]

    while attempts > 0:
        print_face(attempts)
        print(word_with_blanks(word, letters_guessed))
        guessed_letter = input_letter_from_user(letters_guessed)
        letters_guessed.append(guessed_letter)
        if guessed_letter in word:
            if game_is_won(word, letters_guessed):
                break
        else:
            attempts -= 1

    # user loses the game

    if attempts <= 0:
        print_face(0)
        print("GAME OVER!\n")
        print("The correct word was: ", word_with_case)

    # user wins the game

    else:
        attempts = 0
        print(faces[6])
        print("You won the Game.\n")
        print("The correct word is: ", word_with_case)


def main():
    """Responsible for all the things happening while the entire programme is being run"""
    
    play_game = True
    while play_game:
        
        # display categories of words

        print_menu()
        picked_word = category_from_user()
        run_game(picked_word)

        # ask user if he wants to continue playing

        if input("\nContinue (Y)? ").lower() == "n":
            play_game = False
            

if __name__ == "__main__":
    main()
