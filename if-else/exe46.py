# Exercise 46: Season from Month and Day
# The year is divided into four seasons: spring, summer, fall and winter. While the
# exact dates that the seasons change vary a little bit from year to year because of the
# way that the calendar is constructed, we will use the following dates for this exercise:
# Season First day
# Spring March 20
# Summer June 21
# Fall September 22
# Winter December 21
# Create a program that reads a month and day from the user. The user will enter
# the name of the month as a string, followed by the day within the month as an
# integer. Then your program should display the season associated with the date that
# was entered.
season = {1:"Summer",2:"Spring", 3:"Fall", 4:"Winter" }
months_num = {'january':4,
          'february':4,
          'march': 0,
          'april':2,
          'may':2,
          'june':0,
          'july':1,
          'august':1,
          'september':0,
          'october':3,
          'november':3,
          'december':0}

month = input("Enter month :").strip(" ").lower()
day = int(input("Enter day:"))
if months_num[month] == 0:
    if month == 'march':
        print("Spring") if 20<=day<=30 else print("Winter")
    elif month == 'june':
        print("Summer") if 21<=day<=31 else print("Spring")
    elif month == 'september':
        print("Fall") if 22<=day<=30 else print("Summer")
    elif month == 'december':
        print("Winter") if 21<=day<=31 else print("Fall")
else:
    print(season[months_num[month]])