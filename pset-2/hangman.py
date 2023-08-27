# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
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
    print(len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word: str, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # loop through each letter in secret_word
    for letter in secret_word:
        # if the letter is not in letters_guessed, return False
        if letter not in letters_guessed:
            return False
    # if the loop finishes without returning False, return True
    return True

    
def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # loop over characters in secret_word
    string = ''
    for c in secret_word:
      # if the charachter is found add to string, else add ' _ ' instead
      if c in letters_guessed:
          string += c
      else:
          string += ' _ '

    return string


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # get all lowercase letters
    letters_not_guessed = string.ascii_lowercase
    # replace them and update the list of all letters
    for c in letters_guessed:
        letters_not_guessed = letters_not_guessed.replace(c, '')
    
    return letters_not_guessed
            

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print('Welcome to the game Hangman!' + '\n' + 'I am thinking of a words that is', len(secret_word), 'letters long.')
    print('-----------------')

    guesses = []
    warnings = 3
    warning = True
    number_of_guesses = 6
    consonants = 'bcdfghjklmnpqrstvwxyz'
    vowels = 'aeiou'
    completed = False
    while number_of_guesses:

      if warning:
        print(f'You have {warnings} warnings left.')
        warning = False

      print(f'You have {number_of_guesses} guesses left.')
      print('Available letters:', get_available_letters(guesses))
      guess = input('Please guess a letter: ').lower()

      if guess in guesses and warnings > 0:
          warnings -= 1
          warning = True
          print(f"Oops! You've already guessed that letter. You now have {warnings} warnings left: {get_guessed_word(secret_word, guesses)}")
  
      elif guess in secret_word and guess not in guesses:
          guesses.append(guess)
          print('Good guess:', get_guessed_word(secret_word, guesses))

      elif warnings >= 1 and not(guess.isalpha()):
          warnings -= 1
          warning = True
          print(f'Oops! That is not a valid letter. You now have {warnings} warnings left: {get_guessed_word(secret_word, guesses)}')
          
      elif warnings <= 0 and not(guess.isalpha()):
          number_of_guesses -= 1
          print(f'Oops! That is not a valid letter. You now have {number_of_guesses} guesses left: {get_guessed_word(secret_word, guesses)}')
          

      elif warnings <= 0 and guess.isalpha():
          number_of_guesses -= 1
          print(f"Oops!. You've already guessed that letter. You now have {number_of_guesses} guesses left: {get_guessed_word(secret_word, guesses)}")

      else:
          guesses.append(guess)
          if guess in consonants:
              number_of_guesses -= 1
          elif guess in vowels:
              number_of_guesses -= 2
          print('Oops! That letter is not in my word:', get_guessed_word(secret_word, guesses))

      print('-----------------')

      if is_word_guessed(secret_word, guesses):
        completed = True
        print('Congratulations, you won!')

        unique_letters = []
        for letter in secret_word:
            if letter not in unique_letters:
                unique_letters.append(letter)
            else:
                pass
        print('Your total score for this game is:', number_of_guesses * len(unique_letters))
        break
    
    if not completed:
        print(f'Sorry you ran out of gusses. The word was {secret_word}')



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word: str, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    if len(my_word) != len(other_word):
        return False
    
    my_word = my_word.replace(' ', '')
    for i in range(len(my_word)):
        if my_word[i] != '_':
            if my_word[i] != other_word[i]:
                return False
        else:
            if other_word[i] in my_word:
                return False
    return True

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    my_word = my_word.replace(' ', '')
    matches = list()
    for word in wordlist:
        if match_with_gaps(my_word, word):
            matches.append(word)
    if len(matches) == 0:
        print('No matches were found')
    else:
        print('Possible guesses are:\n',matches)
        print('-----------------')
            

def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print('Welcome to the game Hangman!' + '\n' + 'I am thinking of a words that is', len(secret_word), 'letters long.')
    print('-----------------')

    guesses = []
    warnings = 3
    warning = True
    number_of_guesses = 6
    consonants = 'bcdfghjklmnpqrstvwxyz'
    vowels = 'aeiou'
    completed = False
    while number_of_guesses:
      if warning:
        print(f'You have {warnings} warnings left.')
        warning = False

      print(f'You have {number_of_guesses} guesses left.')
      print('Available letters:', get_available_letters(guesses))
      guess = input('Please guess a letter: ').lower()

      if guess == '*':
          show_possible_matches(get_guessed_word(secret_word, guesses))
          continue

      if guess in guesses and warnings > 0:
          warnings -= 1
          warning = True
          print(f"Oops! You've already guessed that letter. You now have {warnings} warnings left: {get_guessed_word(secret_word, guesses)}")
  
      elif guess in secret_word and guess not in guesses:
          guesses.append(guess)
          print('Good guess:', get_guessed_word(secret_word, guesses))

      elif warnings >= 1 and not(guess.isalpha()):
          warnings -= 1
          warning = True
          print(f'Oops! That is not a valid letter. You now have {warnings} warnings left: {get_guessed_word(secret_word, guesses)}')
          
      elif warnings <= 0 and not(guess.isalpha()):
          number_of_guesses -= 1
          print(f'Oops! That is not a valid letter. You now have {number_of_guesses} guesses left: {get_guessed_word(secret_word, guesses)}')
          

      elif warnings <= 0 and guess.isalpha():
          number_of_guesses -= 1
          print(f"Oops!. You've already guessed that letter. You now have {number_of_guesses} guesses left: {get_guessed_word(secret_word, guesses)}")

      else:
          guesses.append(guess)
          if guess in consonants:
              number_of_guesses -= 1
          elif guess in vowels:
              number_of_guesses -= 2
          print('Oops! That letter is not in my word:', get_guessed_word(secret_word, guesses))

      print('-----------------')

      if is_word_guessed(secret_word, guesses):
        completed = True
        print('Congratulations, you won!')

        unique_letters = []
        for letter in secret_word:
            if letter not in unique_letters:
                unique_letters.append(letter)
            else:
                pass
        print('Your total score for this game is:', number_of_guesses * len(unique_letters))
        break
    
    if not completed:
        print(f'Sorry you ran out of gusses. The word was {secret_word}')



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    pass
    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
