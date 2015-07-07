# Hangman game
# Created by: Yuqing Ren

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
    False otherwise
    '''
    for char in secretWord:
        if char not in lettersGuessed:
            return False
    return True

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
    what letters in secretWord have been guessed so far.
    '''
    guessedWord = secretWord
    for char in secretWord:
        if char not in lettersGuessed:
            guessedWord = guessedWord.replace(char, '_ ')
    return guessedWord

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
    yet been guessed.
    '''
    availableLetters = list(string.ascii_lowercase)
    for letter in lettersGuessed:
        availableLetters.remove(letter)
    return ''.join(availableLetters)

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.
    '''
    guess = 8
    lettersGuessed = []
    win = False

    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is %d letters long." %(len(secretWord))

    while guess > 0:
        print "-------------"
        print "You have %d guesses left." %(guess)
        print "Available letters: ", getAvailableLetters(lettersGuessed)
        while True:
            ans = raw_input("Please guess a letter: ").lower()
            if len(ans) > 1 or ans not in string.ascii_lowercase:
                print "I don't understand."
            else:
                break
        if ans in lettersGuessed:
            print "Oops! You've already guessed that letter: ",
        else:
            lettersGuessed.append(ans)
            if ans in secretWord:
                print "Good guess: ",
            else:
                guess -= 1
                print "Oops! That letter is not in my word: ",
        print getGuessedWord(secretWord, lettersGuessed)
        if isWordGuessed(secretWord, lettersGuessed):
            win = True
            break

    print "------------"
    if win == True:
        print "Congratulations, you won!"
    else:
        print "Sorry, you ran out of guesses. The word was %s." %(secretWord)

if __name__ == "__main__":
    # Load the list of words into the variable wordlist
    wordlist = loadWords()
    secretWord = chooseWord(wordlist).lower()
    hangman(secretWord)
