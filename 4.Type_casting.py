#type casting = convert the data type to another data type.
x = 1 #int
y = 2.0 #float
z = "3" #str

print(x)
print(y)
print(z)

print(x)
print(int(y)) #the data type of y was temporarily changed to an integer for this line. when the data type is changed, it prints until it encounters an unknown character,
print (y)
print(z)

y = int(y) #the data type of y was permanently changed to the integer from this line onwards.
print(x)
print(y)
print(z)

print(x)
print(y)
print(z*3) #strings can't be used for math inputs. the console does not take the "3" in string type as a number so it is printed 3 times.
print(int(z)*3)
print(z*3)
z = int(z)
print(z*3)

print(float(x)) #the variables were given a decimal point to show they are converted to a float.
print(float(y))
print(float(z))

print("X is a "+str(x)) #If x is left as an int, we get a syntax error when trying to display this code.
print("Y is a "+str(y)) #we can't print 2 strings of different data types in the same function.
print("Z is a "+str(z))
