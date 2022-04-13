# Exercise 29: Celsius to Fahrenheit and Kelvin
#
# Write a program that begins by reading a temperature from the user in degrees
# Celsius. Then your program should display the equivalent temperature in degrees
# Fahrenheit and degrees Kelvin. The calculations needed to convert between different
# units of temperature can be found on the internet.

celsius = float(input("Enter temperature in degree celsius :"))
print("Equivalent Fahrenheit =", celsius*(9/5)+32)
print("Equivalent Kelvin = ", celsius+273.15)