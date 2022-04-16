# Exercise 39: Sound Levels
# The following table lists the sound level in decibels for several common noises.
# Noise Decibel level (dB)
# Jackhammer 130
# Gas lawnmower 106
# Alarm clock 70
# Quiet room 40
# Write a program that reads a sound level in decibels from the user. If the user
# enters a decibel level that matches one of the noises in the table then your program
# should display a message containing only that noise. If the user enters a number
# of decibels between the noises listed then your program should display a message
# indicating which noises the level is between. Ensure that your program also generates
# reasonable output for a value smaller than the quietest noise in the table, and for a
# value larger than the loudest noise in the table.

dc = int(input("Enter decibel level :"))
if dc>=40 and dc<=70:
    if dc == 40:
        print("Quiet room")
    elif dc == 70:
        print("Alarm clock")
    else:
        print("Its in between Quite room and Alarm clock")
elif dc>70 and dc<=106:
    if dc == 106:
        print("Gas lawnmower")
    else:
        print("Its in between Alarm clock and Gas lawnmower")
elif dc > 106 and dc <= 130:
    if dc == 130:
        print("Jackhammer")
    else:
        print("Its in between Gas lawnmower and Jackhammer")
elif dc<40:
    print("Quietest noise")
else:
    print("Very loud")
