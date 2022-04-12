# Exercise 24: Units of Time
#
# Create a program that reads a duration from the user as a number of days, hours,
# minutes, and seconds. Compute and display the total number of seconds represented
# by this duration.

days = int(input("Enter number of days :"))
hours = int(input("Enter number of hours :"))
minutes = int(input("Enter number of minutes :"))
seconds = int(input("Enter number of seconds"))
print("Total seconds :",seconds + (minutes*60) +(hours*3600) +(days * (24*3600)))
