# Exercise 18:Volume of a Cylinder
# The volume of a cylinder can be computed by multiplying the area of its circular
# base by its height. Write a program that reads the radius of the cylinder, along with
# its height, from the user and computes its volume. Display the result rounded to one
# decimal place.
import math as m
radius = float(input("Enter radius:"))
height = float(input("Enter height:"))
print("Volume of a cylinder = %.1f " %(m.pi*(radius*radius)*height))