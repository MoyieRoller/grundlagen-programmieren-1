while True:
    userInput = input("Please enter a numerical midi-note: ")
    inputNote = None
    rangeTest = None

    # avoid an error if someone enters a string
    try:
        inputNote = int(userInput)
        rangeTest = inputNote + 7
    except ValueError:
        print("ERROR: Not a valid midi-note")
        continue

    # limiting the midi-note range from A0 to C8
    if rangeTest not in range(21, 109):
        print("ERROR: Midi-note out of range")
    else:
        break

# calculating the notes to complete the desired major chord
fundamental = inputNote
major_third = fundamental + 4
fifth = fundamental + 7

# calculating the correct note values
noteValues = ["C", "C#", "D", "Eb", "E", "F", "F#", "G", "G#", "A", "Bb", "B"]
octaves = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]

fundamental_name = noteValues[fundamental % 12] + octaves[int((fundamental / 12) - 1)]
major_third_name = noteValues[major_third % 12] + octaves[int((major_third / 12) - 1)]
fifth_name = noteValues[fifth % 12] + octaves[int((fifth / 12) - 1)]

print("fundamental: " + str(fundamental) + " (" + fundamental_name + ")")
print("major_third: " + str(major_third) + " (" + major_third_name + ")")
print("fifth: " + str(fifth) + " (" + fifth_name + ")")
print("")
print("Is C4 higher than all three notes?")

print(bool(fifth < 60))