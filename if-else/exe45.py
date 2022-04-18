# Exercise 45:What Color is that Square?
# Positions on a chess board are identified by a letter and a number. The letter identifies
# the column, while the number identifies the row, as shown below:
# Write a program that reads a position from the user. Use an if statement to determine
# if the column begins with a black square or a white square. Then use modular
# arithmetic to report the color of the square in that row. For example, if the user enters
# a1 then your program should report that the square is black. If the user enters d5
# then your program should report that the square is white. Your program may assume
# that a valid position will always be entered. It does not need to perform any error
# checking.

col_to_val = {'a':1,
              'b':2,
              'c':3,
              'd':4,
              'e':5,
              'f':6,
              'g':7,
              'h':8 }
pos = input("Enter position :").strip(" ")
#col position 'a' starts with black block so all even rows of that columns will be white
# and odd rows black.
if col_to_val[pos[0].lower()] % 2 == 0:
    print("Black") if int(pos[1])%2 == 0 else print("White")
else:
    print("White") if(int(pos[1]) % 2 == 0) else print("Black")