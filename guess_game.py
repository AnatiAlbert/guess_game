# Guessing Game
'''import random
from art_guess import logo
print(logo)
print('Welcome To The Number Guessing Game!')
print('You Have To Guess A Number Between 1 to 100.')
pickrandom = random.randint(1, 100)
print(pickrandom)
level = input('What difficulty level do you choose? "hard" or "easy": ').lower()

def difficulty_level(level, attempts):
    print(f'You have {attempts} attempts.')
    guess = int(input('Enter the number: '))
    start = False
    while not start:
        attempts -= 1
        if attempts == 0:
            start = True
            print('You have run out of guesses you lose')
        elif guess == pickrandom:
            print(f'You got it, number is {pickrandom}')
            start = True
        elif guess > pickrandom:
            print('Too high')
            print('Guess again')
            print(f'You have {attempts} attempts left')
            guess = int(input('Make another guess again: '))
        elif guess < pickrandom:
            print('Too less')
            print('Guess again')
            print(f'You have {attempts} attempts left')
            guess = int(input('Make another guess again: '))

if level == 'hard':
    difficulty_level('hard', 5)
else:
    difficulty_level('easy', 10)
'''

from random import randint
from art_guess import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
turns = 0

#make function to set difficulty
def set_difficulty():
    level = input('Choose a difficulty. Type "hard" or "easy": ')
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

#function to check user's guess against actual answer
def check_answer(guess, answer, turns):
    '''checks answer against guess. Returns the number of turns remaining'''
    if guess > answer:
        print('Too high.')
        return turns - 1
    elif guess < answer:
        print('Too low.')
        return turns - 1
    else:
        print(f'You got it! The answer was {answer}.')

def game():
    print(logo)
    #choosing a random number 1 qnd 100
    print('Welcome to the Number Guessing Game!')
    print('I am thinking of a number between 1 and 100.')
    answer = randint(1, 100)
    print(f'Pssst, the correct answer is {answer}')

    turns = set_difficulty()

    #Repeat the guessing functionality if they get it wrong
    guess = 0
    while guess != answer:
        print(f'You have {turns} attempts remaining to guess the number.')
        #Let the user guess a number
        guess = int(input('Make a guess: '))

        turns = check_answer(guess, answer, turns)

        #track the number of turns and reduce by if they get it wrong.
        if turns == 0:
            print('You have run out of guesses, you lose.')
            return
game()
