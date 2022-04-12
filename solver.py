from wordList import words
import os

def add_correct_letters(letters, words):
    impossible_words = {'xxxxx'}
    # filter out words that don't have correct letter in correct position
    for i in range(0, len(letters)):
        if letters[i] != '-':
            for word in words:
                if word[i] != letters[i]:
                    impossible_words.add(word)

    for x_word in impossible_words:
        if x_word in words:
            words.remove(x_word)
    return words

def add_possible_letters(letters, words):
    impossible_words = {'xxxxx'}
    # filter out words without these letters
    for word in words:
        for i in range(0, len(letters)):
            if letters[i] != '-':
                if letters[i] not in word:
                    impossible_words.add(word)

    # filter out words with correct letter in wrong position
    for i in range(0, len(letters)):
        if letters[i] != '-':
            for word in words:
                if word[i] == letters[i]:
                    impossible_words.add(word)
        
    for x_word in impossible_words:
        if x_word in words:
            words.remove(x_word)
    return words

def add_incorrect_letters(bad_letters, words):
    impossible_words = {'xxxxx'}
    for word in words:
        for letter in bad_letters:
            if letter in word:
                impossible_words.add(word)

    for x_word in impossible_words:
        if x_word in words:
            words.remove(x_word)
    return words



def main_menu():
    os.system('cls||clear')
    print("Welcome to Wordle Solver")
    while(True):
        print("1. Solve new puzzle")
        print("2. Quit")
        option = input("Selection:")
        if option == '1':
            game_menu()
        elif option == '2':
            print("Goodbye")
            exit()
        else:
            print("\nInvalid input\n")


def game_menu():
    os.system('cls||clear')
    print("##########################")
    print("        New Game")
    print("##########################\n")
    possible_words = words

    while (True):
        print("Options: (input a number to select option)")
        print("1. Enter the known letters in correct positions")
        print("2. Enter the known letters in incorrect positions ")
        print("3. Enter incorrect letters")
        print("4. List Possible words")
        print("5. Main Menu")
        option = input("Selection:")
        os.system('cls||clear')

        if option == '1':
            print("Enter the known letters in the correct position and unknown letters with a \'-\'.")
            print("Example: --e--t")
            knownLetters = input()
            if len(knownLetters) == 5:
                possible_words = add_correct_letters(knownLetters, possible_words)
            else:
                print("Too many letters. Enter only 5 characters. Example: --e--t")
        elif option == '2':
            print("Enter the known letters in the incorrect position and unknown letters with a \'-\'.")
            print("Example: --r-q")
            possibleLetters = input()
            if len(possibleLetters) > 5:
                print('Too many letters')
            else:
                possible_words = add_possible_letters(possibleLetters, possible_words)
        elif option == '3':
            print("Enter the incorrect letters. (No spaces or commas)")
            bad_letters = input()
            if len(bad_letters) > 5:
                print('Too many letters')
            else:
                possible_words = add_incorrect_letters(bad_letters, possible_words)
        elif option == '4':
            print(possible_words)
        elif option == '5':
            return


if __name__ == "__main__":
    main_menu()

