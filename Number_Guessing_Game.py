# invoke the randint function
from random import randint

# create our basic number guessing game
def number_guess(x):
    secret_number = randint(1,x)
    user_guess = 0
    while user_guess != secret_number:
        user_guess = int(input(f'Guess a number between 1 and {x}: '))
        if user_guess > secret_number:
            print(f'{user_guess} is too high. Try again...')
        elif user_guess < secret_number:
            print(f'{user_guess} is too low. Try again...')
    
    print(f'You guessed correctly! The secret number was {secret_number}')

# this project is inspired by those seen in this video: https://www.youtube.com/watch?v=8ext9G7xspg