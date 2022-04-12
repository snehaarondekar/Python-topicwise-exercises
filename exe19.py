# Exercise 19: Free Fall
# (Solved—16 Lines)
# Create a program that determines how quickly an object is traveling when it hits the
# ground. The user will enter the height from which the object is dropped in meters (m).
# Because the object is dropped its initial speed is 0m/s. Assume that the acceleration
# due to gravity is 9.8m/s2.
from math import sqrt
GRAVITY = 9.8
d = float(input("height from which the object is dropped :"))
vf = sqrt(0+2*GRAVITY*d)
print("It will hit the ground at %.2f m/s" %vf)
