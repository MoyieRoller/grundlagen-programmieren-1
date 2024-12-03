user_input = input('Please enter a date int the format DD.MM.YYYY: ').strip()
date = user_input.split('.')

length_list = [2, 2, 4]
i = 0

for i in range(len(date)):
    if len(date[i]) != length_list[i]:
        print('This was not the correct format!')
        break

    if not date[i].isdigit():
        print('This was not the correct format!')
        break

print('Your date was:', date[0] + '.' + date[1] + '.' + date[2])