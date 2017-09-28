#Pedro Gallino
#9/28/17
#numberGuessingGame.py - is a number guessing game

from random import randint

num = randint(1,100)
runs = 0

while True:
    runs += 1
    guess = int(input('Guess a number'))
    if guess > num:
        print('Guess is to high')
    if guess < num:
        print('Guess is to low')
    if guess == num:
        print('The number is', num)
        break
print('You got it in',runs,'tries')
