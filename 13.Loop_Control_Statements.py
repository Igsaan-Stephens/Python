# Loop control statements = change the loop execution from its regular sequence.
# break = terminates the loop entirely
# continue = skips to the next iteration of the loop
# pass = does nothing. Is used as a placeholder

while True:
    name = input("What is your name? ")
    if name != "":
        break

phone_number = "123-456-7890"

for i in phone_number:
    if i == "-":
        continue
    print(i, end="") #make sure to print "i" and not "phone_number"

for i in range(1,21):
    if i == 13: #this code breaks if you put 13 in "" because it's looking for a number 13 but "13" is a string.
        pass
    else:
        print(i)