#Logical operators (and,or,not) = Used to check if mutiple statements are true.
# and = Check if 2 or more statements are both true at the same time.
# or = Used to check if one of multiple statements are true.
# not = Flips a statement from true to false or vise verse.

temp = int(input("What is the temperature today?"))
if temp >= 0 and temp <=30:
    print("The temperature is nice!")
    print("Touch grass!")
elif temp <0 or temp >30:
    print("The temperature is bad!")
    print("Stay indoors!")

weather = int(input("How hot is it today?"))
if not(weather >= 0 and weather <=30):
    print("The weather is bad!")
    print("Stay indoors!")
    
elif not(weather <0 or weather >30):

    print("The weather is nice!")
    print("Touch grass!")
