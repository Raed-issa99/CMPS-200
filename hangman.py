    # Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import string
import random
alphabets = string.ascii_lowercase


WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    for i in secretWord:
        if not (i in lettersGuessed):
            return False
    return True


def getGuessedWord(secretWord, lettersGuessed):
    guessed = ''
    for i in secretWord:
        if i in lettersGuessed:
            guessed += i
        elif not (i in lettersGuessed):
            guessed += '_ '
    return guessed


def getAvailableLetters(lettersGuessed):
    global alphabets
    letters_left = ''
    for i in alphabets:
        if not (i in lettersGuessed):
            letters_left += i
    return letters_left


def hangman(secretWord):
    print("Welcome to your doom! Just kidding, it's hangman! Enjoyy")
    print("I'm thinking of a word that is.... wait for it..",len(secretWord),"letters long")
    lettersGuessed = []
    attempsLeft = 8
    while getGuessedWord(secretWord,lettersGuessed) != secretWord and attempsLeft > 0:
        print("You can screw up",attempsLeft,"more times")
        print("Available letters:",getAvailableLetters(lettersGuessed))
        x = input("Now take your chances and guess a letter: >")
        if x in secretWord and not(x in lettersGuessed):
            lettersGuessed += [x]
            print("You got lucky:",getGuessedWord(secretWord,lettersGuessed))
        elif x in lettersGuessed:
            print("You fool, you already guessed that letter, try again")
        elif not (x in secretWord) and not (x in lettersGuessed):
            lettersGuessed += [x]
            attempsLeft -= 1
            print("That one's wrong, sorry pal:",getGuessedWord(secretWord,lettersGuessed))
        print("----------------------------------------------------------------")
    if getGuessedWord(secretWord,lettersGuessed) == secretWord:
        print("You win..... this timeeee")
    if attempsLeft == 0:
        print("Machines win! You loseee!")
        print("Your word was:",secretWord)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
