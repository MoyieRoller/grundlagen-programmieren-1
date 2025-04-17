class MidiNote:

    def __init__(self, pitch, duration):
        self.pitch = pitch
        self.duration = duration

    def getOctave(self):
        return self.pitch // 12 - 1

    def getFrequency(self):
        return 440 * 2 ** ((self.pitch - 69) / 12)

if __name__ == "__main__":

    n1 = MidiNote(60, 1/4)
    print(f'Octave: {n1.getOctave()}')
    print(f'Frequency: {n1.getFrequency()}')