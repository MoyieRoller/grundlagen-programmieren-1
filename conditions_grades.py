user_input = input('Please enter a grade: ')

if  user_input.isdigit():

    if user_input == '1':
        print('sehr gut')
    elif user_input == '2':
        print('gut')
    elif user_input == '3':
        print('befriedigend')
    elif user_input == '4':
        print('ausreichend')
    elif user_input == '5':
        print('mangelhaft')
    elif user_input == '6':
        print('ungenuegend')
    else:
        print('Not a valid grade!')
else:
    print('Not a natural number!')
