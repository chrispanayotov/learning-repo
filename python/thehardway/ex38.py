# Defines a variable ten_things, which holds 1 string with 6 items
ten_things = "Apples Oranges Crows Telephone Light Sugar"
# Normal print function
print("Wait there are not 10 things in that list. Let's fix that.")
# Defines a variable stuff to hold the var ten_things and also calls func. split
# to split the items using ' ' (space)
stuff = ten_things.split(' ')
# Defines a variable more_stuff to hold 8 items in a list
more_stuff = ["Day", "Night", "Song", "Frisbee", 
              "Corn", "Banana", "Girl", "Boy"]
# Defines a while loop, which loops the items in var stuff, while the number
# of the items is not equal to 10
# Also, Defines a var next_one, which holds more_stuff 
# and calls the functions pop() and append()
# In that way, the loop removes the item at last position in more_stuff 
# and adds it in var stuff until the number of items in stuff is 10 
# (the appended item is placed at last position in ten_things)
# When the list reaches 10 items, the while loop stops, because it loops only
# until the number of items is != 10
while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff:")
# Prints the 2nd item in stuff, which is at position 1
print(stuff[1])
# Prints the last item in stuff, which is at position 9
print(stuff[-1])
# Removes the last item in stuff and returns it
print(stuff.pop())
# The last item in stuff (Corn) is removed by .pop, prints the final list 
# without Corn being in it
print(' '.join(stuff))
# Extracts a slice from the stuff list - that is from element 3 to element 4,
# meaning it does not include element 5. Similar to range(3, 5)
print('#'.join(stuff[3:5]))
