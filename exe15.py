# Exercise 15: Distance Units
#
# In this exercise, you will create a program that begins by reading a measurement
# in feet from the user. Then your program should display the equivalent distance in
# inches, yards and miles. Use the Internet to look up the necessary conversion factors
# if you don’t have them memorized.

INCHES_PER_FEET = 12
YARDS_PER_FEET = 0.33
MILES_PER_FEET = 0.000189394
feet = float(input("Enter value in Feet :"))
print(feet, "feet :",feet*INCHES_PER_FEET,"inches,",feet*YARDS_PER_FEET,"Yards,",feet*MILES_PER_FEET, "Miles")
