user_input = input('Gib Zahl: ')

if user_input.isdigit():
    user_input = int(user_input)
    if user_input in [1, 2, 12]:
        print('Winter')
    elif user_input in [3, 4, 5]:
        print('Spring')
    elif user_input in [6, 7, 8]:
        print('Summer')
    elif user_input in [9, 10, 11]:
        print('Fall')
    else:
        print('Not a valid month.')
else:
    print('Not a valid number.')