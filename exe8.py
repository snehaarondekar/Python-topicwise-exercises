# Exercise 8:Widgets and Gizmos
# An online retailer sells two products: widgets and gizmos. Each widget weighs 75
# grams. Each gizmo weighs 112 grams. Write a program that reads the number of
# widgets and the number of gizmos in an order from the user. Then your program
# should compute and display the total weight of the order.
WIDGETS = 75
GIZMO = 112
num_of_widgets = int(input("Enter number of widgets :"))
num_of_gizmos = int(input("Enter number of gizmos :"))
print("Total weight = ",(WIDGETS * num_of_widgets) + (GIZMO * num_of_gizmos), "grams")
print("In Kgs it is :", float(((WIDGETS * num_of_widgets) + (GIZMO * num_of_gizmos))/1000), "Kg")