# Exercise 11: Fuel Efficiency
# In the United States, fuel efficiency for vehicles is normally expressed in miles-pergallon
# (MPG). In Canada, fuel efficiency is normally expressed in liters-per-hundred
# kilometers (L/100 km). Use your research skills to determine how to convert from
# MPGto L/100 km. Then create a program that reads a value from the user in American
# units and displays the equivalent fuel efficiency in Canadian units.

ONE_MPG = 235.215
mpg = float(input("Enter value in Miles pergallon :"))
liter_per_hun = mpg * ONE_MPG
print("Equivalent liter per hundred of",mpg,"MPG is :",liter_per_hun,"liters-per-hundred")