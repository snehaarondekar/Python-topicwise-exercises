# Exercise 25: Units of Time (Again)

# In this exercise you will reverse the process described in the previous exercise.
# Develop a program that begins by reading a number of seconds from the user.
# Then your program should display the equivalent amount of time in the form
# D:HH:MM:SS, where D, HH, MM, and SS represent days, hours, minutes and seconds
# respectively. The hours, minutes and seconds should all be formatted so that
# they occupy exactly two digits, with a leading 0 displayed if necessary.

sec = int(input("Enter number of seconds : "))
s = sec
days = sec//(24*3600)
sec = sec % (24*3600)
hours = sec//3600
sec = sec%3600
minutes = sec//60
sec = sec%60

print(s,"seconds=",days,"days,",hours,"hours,",minutes,"minutes,",sec,"seconds")

