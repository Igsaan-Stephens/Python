import math #For some reason, the math module needs to be imported before it works.
pi = 3.14
x = 1
y = 2
z = 3

print(round(pi)) #round rounds off the number to the nearest whole number.
print(math.ceil(pi)) #ceil rounds up the value to the nearest whole number.
print(math.floor(pi)) #floor rounds down the value to the nearest whole number.
print(abs(pi)) #abs shows how far a value is from 0. It gives all numbers (including negatives) as positives.
print(pow(pi,2)) #pow raises a value to the power of a given number. Always specify the base number then the exponent.
print(math.sqrt(pi)) #sqrt gives the square root of a value.
print(max(x,y,z)) #max gives the largest number in a set.
print(min(x,y,z)) #min gives the smallest number in a set.