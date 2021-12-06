import random
from termcolor import colored #importing necessary modules to customize our game messages. -BL
from pyfiglet import Figlet
cool_font=Figlet(font='standard') #Utilizing the pyfiglet module we imported -BL
banner=Figlet(font='banner3-D')

#Make game longer -CH
NUM_DIGITS = 4 #Change the amount of digits in the mystery number to 4 -CH
MAX_GUESS = 20 #Double the amount of guesses due to increased difficulty -CH

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
        return 'You escaped!' #Changed the winning message to 'you escaped!' -BL

    clues = [] #Assigning clues to an empty list, prepping for the loop below. -BL
    for i in range(len(guess)): #Creates the loop designed to determine what to respond to guesses 1 through 10 inputed by the players. -BL
        if guess[i] == secretNum[i]: #If player guess is determined to be contained in secretNum, and in the right index position using the loop, return 'Fermi' the amount of numbers in the right position
            clues.append('Fermi') #ie. Fermi Fermi if 2 numbers guessed are in the right positions of secretNum. -BL
        elif guess[i] in secretNum: #If player guess is determined to be contained in the the secretNum but not the right index, as it has already failed the Fermi test
            clues.append('Pico')    #it will return 'Pico' corresponding to the number of digits determined to pass the Pico test. -BL
    if len(clues) == 0: #If no digits guessed match indices of secretNum or digits of secretNum, return 'Bagels'. -BL
        return 'Metallica:)'

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

# Tells user the basic rules of the game -CH
print(colored(banner.renderText('Uh-Oh!'), 'red')) 
print(colored("You are trapped in a room. The door is locked with a %s-digit code lock." % (NUM_DIGITS), 'green'))
print(colored('However, every wrong guess gives you clues to what the code is. They are as follows...', 'green'))
print(colored('  If this is the clue:     That means:', 'yellow'))
print(colored('  Metallica:)                None of the digits are correct.', 'blue')) #Changed the message corresponding to no correct digits to 'Metallica'. -BL
print(colored('  Pico                       One digit is correct but in the wrong position.', 'blue'))
print(colored('  Fermi                      One digit is correct and in the right position.', 'blue'))

while True: # Infinite loop -CH
    secretNum = getSecretNum() # Assigns the value of getSecretNum() function to 'secretNum' variable -CH
    
    print(colored(cool_font.renderText('You have %s guesses before the door locks permanently' % (MAX_GUESS)), 'magenta')) # Tells the user that they have MAX_GUESS guesses to guess the mystery number -CH

    guessesTaken = 1 # Assigns 1 to the variale 'guessesTaken'
    while guessesTaken <= MAX_GUESS: # Runs the code below while the value of the variable 'guessesTaken' is less than or equal to MAX_GUESS (in this case 10) -CH
        guess = '' # Assigns a blank string to the variable guess -CH
        while len(guess) != NUM_DIGITS or not isOnlyDigits(guess): # Runs the code below while the users guess is not the correct amount of digits; or while the users guess is not a string of only digits -CH
            print('Guess #%s: ' % (guessesTaken)) # Tells the user which guess they are making (e.g. 'Guess #1:' for their first guess) -CH
            guess = input() # Queries the user to input their guess -CH

        print(getClues(guess, secretNum)) # Prints the clues or if the user guessed the number correctly -CH
        guessesTaken += 1 # Upps the value of 'guessesTaken' by 1 -CH

        if guess == secretNum: # Runs code below if the user guessed the secret number correctly -CH
            break #Stops the loop -CH
        if guessesTaken > MAX_GUESS: # Runs the code below if the user used up all their guesses -CH
            print(colored('You failed to escape... The answer was %s.' % (secretNum), 'red')) # Tells the user they ran out of guesses & the correct secret number -CH

    print('Do you want to play again? (yes or no)') # Asks the user if they want to play again -CH
    if not input().lower().startswith('y'): # Queries the user to input if they want to play again, makes the input lowercase, then checks if the input starts with 'y' -CH
        print('Did you like the game?') 
        if input().lower().startswith('y'):
            print(colored(cool_font.renderText('Thanks! Please give us a good grade!:)'), 'red')) #Utilizing the imported modules to specialize messages! - BL
            break #After the user has rated the game, the loop will break and the game will end. -BL
        else:
            break
