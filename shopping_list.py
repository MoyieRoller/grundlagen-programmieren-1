shopping_list = []

while len(shopping_list) <= 4:
    user_input = input('Please insert items into the shopping list: ')
    shopping_list.append(user_input)

def ex_1(input_list):
    copy_list = input_list[:]
    local_list = input_list
    local_list[1] = 'cornflakes'
    print('EXERCISE 1: exchanged ' + copy_list[1] + ' for ' + local_list[1])
    return local_list

def ex_2(input_list):
    local_list = input_list
    del local_list[-1]
    print('EXERCISE 2: deleted last element of list')
    return local_list

def ex_3(input_list):
    print('EXERCISE 3: print all items on list')
    for item in input_list:
        print(item)

def ex_4(input_list):
    print('EXERCISE 4: print the first three items on list')
    for item in input_list[:3]:
        print(item)

def ex_5(input_list):
    local_list = input_list[::-1]
    print('EXERCISE 5: print all items on list in reversed order')
    for item in local_list:
        print(item)

print("")
print(ex_1(shopping_list))
print("")
print(ex_2(shopping_list))
print("")
ex_3(shopping_list)
print("")
ex_4(shopping_list)
print("")
ex_5(shopping_list)