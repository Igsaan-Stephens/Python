#Slicing = create a substring by extracting elements from another string.
#indexing[] or slice()
#[start:stop:step] Note: starting index is inclusive of the specified character while stopping index is exclusive of specified character. step changes how much we increase the index by between start and stop.
#indexing starts at 0 for the positive index. Positive indexing counts from left to right.
#indexing starts at -1 for the negative index. Negative indexing counts from right to left.

name = "Igsaan Stephens"
first_name = name[0:6] #if first character is used, the code can be written as name[:6]
last_name = name[7:15] #if last character is used, the code can be written as name[7:]
alias = name[0:15:2] #the step means we will only display every 2nd character. By default, the step is 1.
reverse_name = name[::-1] #if the step is negative, it displays the string in reverse.
print(first_name)
print(last_name)
print(alias)
print(reverse_name)

website1 = "http://google.com"
website2 = "http://wikipedia.com"
slice = slice(7,-4) #slice is used to extract a portion of a string and make it reusable for different applications. The given example removes the first 6 characters and the last 4 characters.
print(website1[slice])
print(website2[slice])