# Exercise 14: Height Units

# Many people think about their height in feet and inches, even in some countries that
# primarily use the metric system. Write a program that reads a number of feet from
# the user, followed by a number of inches. Once these values are read, your program
# should compute and display the equivalent number of centimeters.
# Hint: One foot is 12 inches. One inch is 2.54 centimeters.

INCH_PER_FOOT = 12
CM_PER_INCHES = 2.54
feet = int(input("Feet:"))
inches = int(input("Inches :"))
print(feet,"feet",inches,"inches=", ((feet*INCH_PER_FOOT)+inches)*CM_PER_INCHES)
