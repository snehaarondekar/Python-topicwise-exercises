# Exercise 4:Area of a Field
# Create a program that reads the length and width of a farmer’s field from the user in
# feet. Display the area of the field in acres.
# Hint: There are 43,560 square feet in an acre.

SQRFEET_PER_ACRE = 43560
width = float(input("Enter width of the field :"))
length = float(input("Enter length of the field :"))
area = length * width
print("Area of field is ", area/SQRFEET_PER_ACRE, "acre")
