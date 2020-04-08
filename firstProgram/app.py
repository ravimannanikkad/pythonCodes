
# Writen By Ravi Damodaran #
# Python Lists Tutorial
# Working with Lists #

#creating a list of friends here
friends =["Ammu","Appu","Ramu","June","Ammu","Mahesh","Ravi","Aravind"]
#creating a list of lucky numbers here
lucky_numbers=[4,58,5,9,6,7,3,78]

# print the firends list and lucky numbers
print("Print the list friends: ", end= ": ")
print(friends)
print("Print the list lucky numbers: ", end= ": ")
print(lucky_numbers)

# Adding an element to the end of the friends list
print("Append the name \"Aparna\" to the end of friends list", end= ": ")
friends.append("Aparna")
print(friends)

# Adding an element to the middle of the friends list

print("Add the name \"Amrita\" to the index 4", end= ": ")
friends.insert(4,"Amrita")
print(friends)

# Removing an element from the list
print("Remove the name \"June\" from the list", end= ": ")
friends.remove("June")
print(friends)

# Finding the index of an item in the list if it exists
print("Finding the index of name \"Amrita\" from the list", end= ": ")
print(friends.index("Amrita"))

# Counting the number of times the same element exist
print("NUmber of \"Ammu\" in the list", end= ": " )
print(friends.count("Ammu"))

# Sorting the list in ascending order
print("Sorting the friends list in ascending order", end= ": " )
friends.sort()
print(friends)

# Sorting the list in ascending order
print("Sorting the lucky numbers list in ascending order", end= ": " )
lucky_numbers.sort()
print(lucky_numbers)

# Appending the friends list with lucky numbers
print("The extended/ Appended list of of friends with lucky numbers: ", end= ": ")
friends.extend(lucky_numbers)
print(friends)

# Removing all the values from the list
print("Removing all the values from list", end= ": ")
friends.clear()
print(friends)