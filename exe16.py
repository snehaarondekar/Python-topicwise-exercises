# Exercise 16:Area and Volume
# Write a program that begins by reading a radius, r , from the user. The program will
# continue by computing and displaying the area of a circle with radius r and the
# volume of a sphere with radius r . Use the pi constant in the math module in your
# calculations.

# Hint: The area of a circle is computed using the formula area = πr 2. The
# volume of a sphere is computed using the formula volume = 4/3πr 3.

import math as m
radius = float(input("Enter radius :"))
print("The area of circle = ",m.pi*(radius*radius))
print("Volume of sphere =", (4/3)*m.pi*(radius*radius*radius))