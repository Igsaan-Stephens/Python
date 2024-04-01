# tuple = collection which is ordered and unchangeable. Used to group together related data.
# tuple = similar to lists but are written with () instead of [] and they can't be changed later in the code.
student = ("igsaan",24,"male") 

print(student.count("igsaan")) #Tuple.count counts the number of times a variable appears in the tuple.

print(student.index("male")) #Tuple.index gives the position of a given variable in the tuple.

for i in student:
    print(i)

if "igsaan" in student: #used to check if a variable is present in the tuple.
    print("Igsaan is here!")