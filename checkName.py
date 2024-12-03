while True:
    user_input = input('Please enter your first name: ')
    name = user_input.strip()
    if name.isalpha() and name.istitle():
        print('The german Standesamt approves', name, 'as your name!')
        break
    else:
        print('The german Standesamt does not approve', name, 'as your name, please enter a new one!')
        continue