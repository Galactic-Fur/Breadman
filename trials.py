import random
from words_with_category import word_collection as wc

rand_word = random.choice(wc[list(wc.keys())[3]]).lower()

rand_word_list = list(set(rand_word))
letters_list = []


def rep_wth__(word, letter_list=[]):
    replaced = ""
    for letter in word:
        if letter.isalnum():
            if letter.lower() in letter_list:
                replaced += letter.upper() + " "
            else:
                replaced += "_ "
        else:
            replaced += letter + " "

    print(replaced)


while True:
    rep_wth__(rand_word, letters_list)

    ask = input("Letter: ").strip().lower()

    if ask in rand_word:
        letters_list.append(ask)
