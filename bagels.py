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
        return 'You got it!' #When the player guesses the correctly ordered 3 digits, return 'You got it!' -BL

    clues = [] #Assigning clues to an empty list, prepping for the loop below. -BL
    for i in range(len(guess)): #Creates the loop designed to determine what to respond to guesses 1 through 10 inputed by the players. -BL
        if guess[i] == secretNum[i]: #If player guess is determined to be contained in secretNum, and in the right index position using the loop, return 'Fermi' the amount of numbers in the right position
            clues.append('Fermi') #ie. Fermi Fermi if 2 numbers guessed are in the right positions of secretNum. -BL
        elif guess[i] in secretNum: #If player guess is determined to be contained in the the secretNum but not the right index, as it has already failed the Fermi test
            clues.append('Pico')    #it will return 'Pico' corresponding to the number of digits determined to pass the Pico test. -BL
    if len(clues) == 0: #If no digits guessed match indices of secretNum or digits of secretNum, return 'Bagels'. -BL
        return 'Bagels'

    clues.sort() 
    return ' '.join(clues) #Return clues concatenated with a ' ' between each after the loop has finished running. -BL
def isOnlyDigits(num):
    # Returns True if num is a string of only digits. Otherwise, returns False.
    if num == '':
        return False #Test to determine if player input is a series of numbers, otherwise return false. -BL

    for i in num:
        if i not in '0 1 2 3 4 5 6 7 8 9'.split(): #Essentially checks if player inputed 3 digits, otherwise return false. -BL
            return False

    return True

# Print strings explaining rules of game -CH
print('I am thinking of a %s-digit number. Try to guess what it is.' % (NUM_DIGITS))
print('The clues I give are...')
print('When I say:    That means:')
print('  Bagels       None of the digits is correct.')
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
