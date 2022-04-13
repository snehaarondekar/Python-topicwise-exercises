# Exercise 30: Units of Pressure
# In this exercise you will create a program that reads a pressure from the user in kilopascals.
# Once the pressure has been read your program should report the equivalent
# pressure in pounds per square inch, millimeters of mercury and atmospheres. Use
# your research skills to determine the conversion factors between these units

PER_KPASKAL_POUNDSQINCH = 0.145
PER_KPASKAL_MILIMETERS = 7.50062
PER_KPASKAL_ATMOSPHERE = 0.00986923
kp = float(input("Enter pressure in kilopascals :"))
print("Equivalent pressure in pounds per square inch :", kp*PER_KPASKAL_POUNDSQINCH)
print("Equivalent millimeters of mercury :", kp*PER_KPASKAL_MILIMETERS)
print("Equivalent atmosphere :", kp*PER_KPASKAL_ATMOSPHERE)