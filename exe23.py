# Exercise 23:Area of a Regular Polygon
#
# A polygon is regular if its sides are all the same length and the angles between all of
# the adjacent sides are equal. The area of a regular polygon can be computed using
# the formula, where s is the length of a side and n is the number of sides:
# Write a program that reads s and n from the user and then displays the area of a
# regular polygon constructed from these values.
import math as m
s = float(input("Enter lenghth of a side: "))
n = int(input("Enter number of sides: "))
print("Area of polygon = ",(n*(s*s))/(4*m.tan(m.pi/n)))