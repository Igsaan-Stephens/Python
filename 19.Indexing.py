# index operator [] = gives acess to a sequence's element (str, list, tuples)

name = "igsaan Stephens!"


# if(name[0].islower()): # the index checks the character at the specified location. counts from 0.
#    name = name.capitalize()
first_name = name[0:6].capitalize() # you can specifiy a range but the last character isn't included.
last_name = name[7:].lower() # when the range end at the last position, you don't need to specify the end.
full_name = name[:15].upper() # when the range starts at the first position, you don't need to specify the start.
last_character = name[-1] # negative indexing counts from the right side.
print(first_name)
print(last_name)
print(full_name)
print(last_character)
