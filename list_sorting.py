ultra_mega_list = []
while True:
    user_input = input('Please insert list elements: ')
    if user_input.lower() == 'exit':
        break
    else: ultra_mega_list.append(user_input)

ultra_mega_list.sort()
print(ultra_mega_list)