userInput = input('Please enter a valid palindrome: ')
processedString = userInput.lower().strip()

for char in userInput:
    if not char.isalnum():
        processedString = processedString.replace(char, '')

isPalindrome = processedString == processedString[::-1]

print(f'\'{userInput}\' is{" " if isPalindrome else " not "}a palindrome, have a look a this: {processedString}.)')