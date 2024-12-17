dictionary = {}

def print_input(dict):
    pairs = []
    for key, value in dict.items():
        pairs.append((key, value))
    pairs.sort()
    pairs = sorted(pairs, key=lambda x: x[1], reverse=True)
    
    for i in range(len(pairs)):
        tuple = pairs[i]
        print(f'{tuple[1]}: {tuple[0]}')

while True:
    userInput = input('Please insert a string: ')
    if userInput == '':
        print('ending...\n')
        print_input(dictionary)
        break
    else:
        count = dictionary.get(userInput, 0)
        count += 1
        dictionary.update({userInput: count})