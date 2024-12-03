import random
import json

def writescore(score):
    with open('scores.json', 'wb') as f:
        f.write(score)

counter = 0
randomNumber = random.randint(1, 100)

name = input('Please enter your player name: ')

while True:
    userInput = input('Guess a number between 1 and 100. Type for --help for instructions: ')

    if userInput == '--help':
        print('--score : shows list of all scores.\n--highscore : shows to current highscores')

    elif userInput.isdigit():
        userInput = int(userInput)
        if userInput == 0:
            print('Exiting the game...')
            break

        elif userInput > randomNumber:
            counter += 1
            print("You're close", name, "but your number is too high :(")

        elif userInput < randomNumber:
            counter += 1
            print("Sadly your number ist too low,", name, ":/")

        else:
            counter += 1
            gameStats = name + ": " + str(counter) + "\n"
            writescore(gameStats)
            print("Well done " + name + " ! You guessed the correct number and took {} tries.".format(counter))
            break

    else:
        print('You know how to insert a number! Come on, you can do it, try again!')