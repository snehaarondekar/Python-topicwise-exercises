# Exercise 37:Name that Shape
# Write a program that determines the name of a shape from its number of sides. Read
# the number of sides from the user and then report the appropriate name as part of
# a meaningful message. Your program should support shapes with anywhere from 3
# up to (and including) 10 sides. If a number of sides outside of this range is entered
# then your program should display an appropriate error message.

# number_of_sides = int(input("Please enter number of sides :"))
# if number_of_sides == 3:
#     print("Its Triangle")
# elif number_of_sides == 4:
#     print("Its Square")
# elif number_of_sides == 5:
#     print("Its Pantagon")
# elif number_of_sides == 6:
#     print("Its Hexagon")
# elif number_of_sides == 7:
#     print("Its Heptagon")
# elif number_of_sides == 8:
#     print("Its Octagon")
# elif number_of_sides == 9:
#     print("Its Nonagon")
# elif number_of_sides == 10:
#     print("Its Decagon")
# else:
#     print("Wrong input")


number_of_sides = int(input("Please enter number of sides :"))
num_of_sides_shape = {3:"Triangle",4:"Square",5:"Pentagon",6:"Hexagon",7:"Heptagon", 8:"Octagon",9:"Nonagon",10:"Decagon"}
if number_of_sides in num_of_sides_shape:
    print("It is",num_of_sides_shape[number_of_sides])
else:
    print("Wrong Input")
