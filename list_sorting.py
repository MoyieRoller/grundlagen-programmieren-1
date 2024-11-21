coole_liste = []
while True:
    user_input = input('Please insert list elements: ')
    if user_input.lower() == 'exit':
        break
    else: coole_liste.append(user_input)

coole_liste.sort()
print(coole_liste)