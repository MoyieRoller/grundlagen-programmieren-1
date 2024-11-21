ultra_mega_list = []
while True:
    user_input = input('Please insert list elements: ')
    if user_input.lower() == 'exit':
        ultra_mega_list.sort()
        break
    elif user_input == 'show_list':
        print(ultra_mega_list)
    else:
        if user_input.startswith('/'):
            user_input = user_input.lstrip('/')
            if user_input in ultra_mega_list:
                index = ultra_mega_list.index(user_input)
                ultra_mega_list.pop(index)
            else:
                print('Item to remove not in list!')
        else:
            ultra_mega_list.append(user_input)

print(ultra_mega_list)