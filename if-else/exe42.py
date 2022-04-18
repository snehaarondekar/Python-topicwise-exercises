# Exercise 42: Frequency To Note
# In the previous question you converted from note name to frequency. In this question
# you will write a program that reverses that process. Begin by reading a frequency
# from the user. If the frequency is within one Hertz of a value listed in the table in
# the previous question then report the name of the note. Otherwise report that the
# frequency does not correspond to a known note. In this exercise you only need to
# consider the notes listed in the table. There is no need to consider notes from other
# octaves.
note_freq = {"C4": 261.63,
              "D4": 293.66,
              "E4": 329.63,
              "F4": 349.23,
              "G4": 392.00,
              "A4": 440.00,
              "B4": 493.88 }
freq = float(input("Enter frequency : "))
if freq in list(note_freq.values()):
    print((list(note_freq.keys())[list(note_freq.values()).index(freq)]))
else:
    nearest_val = min(list(note_freq.values()), key=lambda x: abs(x-freq))
    if nearest_val-1 <= freq <= nearest_val+1:
        print((list(note_freq.keys())[list(note_freq.values()).index(nearest_val)]))
    else:
        print("The frequency does not correspond to a known note")