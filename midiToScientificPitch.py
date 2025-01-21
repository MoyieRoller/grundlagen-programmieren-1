userInput = input('Please enter a valid midi note: ')

noteNames = ('C', 'C#', 'D', 'D#', 'E', 'F', 'G', 'G#', 'A', 'A#', 'B')

def get_notename_octave(midiNote):
    print(get_notename(midiNote), get_octave(midiNote))

def get_notename(midiNote):
    return noteNames[midiNote % 12]

def get_octave(midiNote):
    return midiNote // 12 - 1

get_notename_octave(int(userInput))
