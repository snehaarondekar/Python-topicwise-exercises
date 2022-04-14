# Exercise 36:Vowel or Consonant
#
# In this exercise you will create a program that reads a letter of the alphabet from the
# user. If the user enters a, e, i, o or u then your program should display a message
# indicating that the entered letter is a vowel. If the user enters y then your program
# should display a message indicating that sometimes y is a vowel, and sometimes y is
# a consonant. Otherwise your program should display a message indicating that the
# letter is a consonant.

alpha = input("Enter a character :")
if alpha.lower() == 'y':
    print("Sometimes",alpha," is a vowel, and sometimes ",alpha," is a consonant")
elif alpha.lower() in ('a','e','i','o','u'):
    print("Entered letter is a vowel")
else:
    print("Entered letter is a consonant")
