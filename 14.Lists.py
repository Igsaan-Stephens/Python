# List = used to store multiple items in a single variable
# to store items in a list, surround the items in [].
# lists can be updated later in the program.

food = ["pizza","burger","hot dog","spaghetti"]

print(food) #prints the entire list.

print(food[1]) #the index is used to print only one element in the list. NB: computers start at 0.

food[1] = "sushi" #the list element 1 was changed from "burger" to "sushi".

print(food[1])

for i in food:
    print(i)

food.append("ice cream") #List.append is used to add a element to the list at the end.

for i in food:
    print(i)

food.remove("hot dog") #List.remove is used to remove a element from a list.

for i in food:
    print(i)

food.pop() #List.pop is used to remove the last element from a list.

for i in food:
    print(i)

food.insert(1,"cake") #List.insert is used to add a element at a specific position in the list.

for i in food:
    print(i)

food.sort() #List.sort is used to sort a list alphabetically.

for i in food:
    print(i)

food.clear() #List.clear is used to remove all element from the list.

print(food)