# Exercise 35: Dog Years
#
# It is commonly said that one human year is equivalent to 7 dog years. However this
# simple conversion fails to recognize that dogs reach adulthood in approximately two
# years. As a result, some people believe that it is better to count each of the first two
# human years as 10.5 dog years, and then count each additional human year as 4 dog
# years.
# Write a program that implements the conversion from human years to dog years
# described in the previous paragraph. Ensure that your program works correctly for
# conversions of less than two human years and for conversions of two or more human
# years. Your program should display an appropriate error message if the user enters
# a negative number.


hy = int(input("Enter years :"))
hm = int(input("Enter months :"))

if hy<0 or hm<0:
    print("Years and months should be positive integer numbers ")
    exit()
dog_age_year_multiplyr = 10.5
dog_age_2years_plus_multiplyr = 4
human_age_months = hy*12+hm
if hy <= 2:
    dog_age_months = dog_age_year_multiplyr * human_age_months
else:
    dog_age_months = dog_age_year_multiplyr * 24 + dog_age_2years_plus_multiplyr * (human_age_months - 24)
dy = dog_age_months // 12
dm = dog_age_months % 12
print("Equivalent dog years as ", int(dy), "years", int(dm), "months")


