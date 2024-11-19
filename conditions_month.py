user_input = input('Please enter a month as a number: ')

if user_input.isdigit():
    if int(user_input) in range(1, 13):
        if int(user_input) in range (3, 6):
            print(str(user_input) + ' ist im Fruehling')
        elif int(user_input) in range (6, 9):
            print(str(user_input) + ' ist im Sommer')
        elif int(user_input) in range (9, 12):
            print(str(user_input) + ' ist im Herbst')
        else:
            print(str(user_input) + ' ist im Winter')
    else:
        print('Not a valid month.')
else:
    print('Please enter a real number.')



