# set = collection which is unordered, unindexed and doesn't allow duplicates.
# set = called using {}

utensils = {"fork", "Spoon", "knife", "knife", "knife", "knife", "knife", "knife"}
dishes = {"bowl","plate","cup","knife"}
#utensils.add("napkin") # set.add is used to add an element to the set.

#for i in utensils:  # The order of elements printed may differ from the order they were written in.
  #  print(i) 
                    # sets are faster than lists

#utensils.remove("fork") # set.remove is used to remove an element from the set.
#for i in utensils:
   # print(i)

#utensils.clear()
#print(utensils)

#utensils.update(dishes) #set.update is used to add a set to another.
#for i in utensils:
#    print(i)

#dinner_table = utensils.union(dishes) # set.union is used to merge multiple sets together.
#for i in dinner_table:
#    print(i)

print(utensils.difference(dishes)) # set.difference is used to compare which elements are not present in both sets.

print(utensils.intersection(dishes)) # set.intersection is used to display which elements are present in both sets.