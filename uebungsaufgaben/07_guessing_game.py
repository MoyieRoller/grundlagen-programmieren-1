import random
import json
from itertools import count


def writescore(score):
    with open('scores.json', 'w') as f:
        json.dump(score, f)

def readscore():
    with open('scores.json', 'r') as f:
        return json.load(f)

counter = 0
randomNumber = random.randint(1, 100)

name = input('Please enter your player name: ')

while True:
    userInput = input('Guess a number between 1 and 100. Type for --lastscore to show the score of the last game: ')

    if userInput == '--score':
        lastscore = readscore()
        print('Last game played by', lastscore["name"], ':', lastscore["score"], 'tries')
        continue

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
            result_dict = {'name': name, 'score': counter}
            writescore(result_dict)
            print("Well done " + name + " ! You guessed the correct number and took {} tries.".format(counter))
            break

    else:
        print('You know how to insert a number! Come on, you can do it, try again!')