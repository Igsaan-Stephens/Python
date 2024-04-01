# dictionary = changeable, unordered collection of unique key:value pairs.
#               Fast because they use hashing, allow us to access a value quickly.

capitals = {'USA':'Washington DC','India':'New Dehli','China':'Beijing','Russia':'Moscow'}

print(capitals['Russia']) # dictionary[Key] returns the value associated with the given key.

print(capitals.get('Germany')) # dictionary.get checks if a value is in the dictionary.
                                # dictionary.get is safer because if a value does not exit, the flow is not interrupted.
print(capitals.keys()) # dictionary.keys returns only the key values.

print(capitals.values()) # dictionary.values only returns the values.

print(capitals.items()) # dictionary.items returns the whole dictionary.



capitals.update({'Germany':'Berlin'}) # dictionary.update can be used to add values.
capitals.update({'USA':'Las Vegas'})  # dictionary.update can also be used to edit values.
capitals.pop('China') # dictionary.pop is used to remove a key:value pair from the dictionary.

for key,values in capitals.items(): #this for loop prints the entire dictionary.
    print(key , values)

capitals.clear() # dictionary.clear is used to delete a dictionary.


