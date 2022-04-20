# write a prog to remove i’th character from string in Python

# string = input("Enter String :")
# index = int(input("Enter index :"))
# str1 = string[:index]
# str2 = string[index+1:]
# output = str1+str2
# print(output)

string = input("Enter String :")
index = int(input("Enter index :"))
print(string[:index]+string[index+1:])
