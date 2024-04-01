#if statement = a block of code that will execute if its condition is true.

age = int(input("how old are you?"))
if age == 100: #The if statement is always checked first. If line 6 was before this line, there would be no way of printing "You are a century old!".
    print("You are a century old!")
elif age >= 18: #All other checks (besides the last one) is given an elif function. You can have any number of elifs.
    print("You are an adult!")
elif age < 0:
    print("You aren't born yet!")
else: #The final check will be an else statement. Imagine this as a last resort.
    print("You are a child!")