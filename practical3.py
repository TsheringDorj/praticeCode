print('Welcome to the guessing game ')

# Ask the user the name and store it in userName box (variable)
userName = input('What is your name? ')

print('Welcome. ', userName, 'lets play a gussing game') 

tries = 1

secretNumber = '9'

guess = input('Guess a number from 1 to 10 ')

if guess == secretNumber:
    print('Your guess is correct!')
    print('Tries: ', tries)
    print('Game Over!')
    exit()
else:
    tries = tries + 1
    print('Try again')

guess = input('Guess a number from 1 to 10 ')

if guess == secretNumber:
    print('Your guess is correct!')
    print('Tries: ', tries)
    print('Game Over!')
    exit()
else:
    tries = tries + 1
    print('Try again')

guess = input('Guess a number from 1 to 10 ')

if guess == secretNumber:
    print('Your guess is correct!')
    print('Tries: ', tries)
    print('Game Over!')
    exit()
else:
    print('Game Over!')

    