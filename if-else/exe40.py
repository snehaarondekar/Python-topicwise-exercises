# Exercise 40:Name that Triangle
# A triangle can be classified based on the lengths of its sides as equilateral, isosceles
# or scalene. All 3 sides of an equilateral triangle have the same length. An isosceles
# triangle has two sides that are the same length, and a third side that is a different
# length. If all of the sides have different lengths then the triangle is scalene.
# Write a program that reads the lengths of 3 sides of a triangle from the user.
# Display a message indicating the type of the triangle.

sides = tuple(input("Enter length of 3 sides of the triangle : ").strip(" ").split(","))
print(sides)
if len(set(sides)) == 3:
    print("scalene")
elif len(set(sides)) == 2:
    print("isosceles Triangle")
else:
    print("Equilateral Triangle")