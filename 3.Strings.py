#Strings can be formatted in a few different ways. 
name = "iGsAaN"
age = "23"
birth = "26 December"
print(name)
print(len(name))
#len gives the number of characters in the string.
print(name.find("s"))
#find locates the position of the given character in the string. the counting starts at 0.
print(name.capitalize())
#capitalize capitalizes the first letter in the string.
print(name.upper())
#upper gives the string in only upper case letters.
print(name.lower())
#lower gives the string in only lower case letters.
print(name.isdigit())
print(birth.isdigit())
print(age.isdigit())
#isdigit is used to check if the string contains only digits.
print(name.isalpha())
print(birth.isalpha())
print(age.isalpha())
#isalpha is used to check if the string contains only letters.
print(name.count("a"))
print(birth.count("e"))
#count is used to count the number of a specific character in the string. the character listed is case sensitive.
print(name.replace("i","1"))
#replace is used to swap out characters in the string.
print(name*3)
#* is used to give the string multiple times.

