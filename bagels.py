import random

NUM_DIGITS = 3 #Amount of digits for mystery number -CH
MAX_GUESS = 10 #Amount of guesses -CH

def getSecretNum():
    # Returns a string of unique random digits that is NUM_DIGITS long.
    
    numbers = list(range(10)) # Assigns a list of range 10 to 'numbers' variable -CH
    
    random.shuffle(numbers) # Shuffles the list 'numbers' in place and returns None -CH
    
    secretNum = '' # Assigns a blank string to the 'secretNum' variable -CH
    
   
    for i in range(NUM_DIGITS): # For every index in a range of NUM_DIGITS...
        #Concatenates the first NUM_DIGITS(in this case three) index values from the shuffled 'numbers' converted into a string; -CH
        #Concatenates it with the blank string 'secretNum' and reassigns the new string to 'secretNum' -CH
        secretNum += str(numbers[i]) 
    return secretNum # Returns variable 'secretNum' -CH

def getClues(guess, secretNum):
    # Returns a string with the Pico, Fermi, & Bagels clues to the user.
    if guess == secretNum:
        return 'You got it!'

    clues = []
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'

    clues.sort()
    return ' '.join(clues)
def isOnlyDigits(num):
    # Returns True if num is a string of only digits. Otherwise, returns False.
    if num == '':
        return False

    for i in num:
        if i not in '0 1 2 3 4 5 6 7 8 9'.split():
            return False

    return True

# Print strings explaining rules of game -CH
print('I am thinking of a %s-digit number. Try to guess what it is.' % (NUM_DIGITS))
print('The clues I give are...')
print('When I say:    That means:')
print('  Bagels      None of the digits is correct.')
print('  Pico         One digit is correct but in the wrong position.')
print('  Fermi        One digit is correct and in the right position.')

while True:
    secretNum = getSecretNum()
    print('I have thought up a number. You have %s guesses to get it.' % (MAX_GUESS))

    guessesTaken = 1
    while guessesTaken <= MAX_GUESS:
        guess = ''
        while len(guess) != NUM_DIGITS or not isOnlyDigits(guess):
            print('Guess #%s: ' % (guessesTaken))
            guess = input()

        print(getClues(guess, secretNum))
        guessesTaken += 1

        if guess == secretNum:
            break
        if guessesTaken > MAX_GUESS:
            print('You ran out of guesses. The answer was %s.' % (secretNum))

    print('Do you want to play again? (yes or no)')
    if not input().lower().startswith('y'):
        break
