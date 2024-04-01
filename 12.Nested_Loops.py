# nested loop = A loop that is contained inside of another loop. The both loops can be either for or while. The
#              "inner loop" will finish all of its iterations before finishing one iteration of the "outer loop".

rows = int(input("How many rows?: ")) #input is always stored as a string.
columns = int(input("How many columns? "))
symbol = input("Enter a symbol to use: ")

for i in range(rows): # when writing a loop, the "i" can be replaced with any character but i is just most common.
    for j in range(columns):
        print(symbol, end="")
    print()