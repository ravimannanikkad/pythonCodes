
# Writen By Ravi Damodaran #
# Python String Tutorial
# Working with Strings #


phrase = "Ravi Mannanikkad"
#1 Printing a Variable 1
print("1", end =": ")
print(phrase)
#2 String Concantination 2
print("2", end =": ")
print(phrase + " is fantastic")
#3 Using a built in function of strings 3
print("3", end =": ")
print(phrase.upper())
#4 Checking if the phrase us uppercase or not 4
print("4", end =": ")
print(phrase.isupper())

#5 Pipelining functions where convert to lower case
# and check if it is lowercase 5
print("5", end =": ")
print(phrase.lower().islower())

#6 Length of string 6
print("6", end =": ")
print(len(phrase))

#7 Fetching a character in string 7
print("7", end =": ")
print(phrase[0])

#8 Getting index of a character (i) from string 8
print("8", end =": ")
print(phrase.index("i"))

#9 Getting index of a substring (Mannanikkad) from string 9
print("9", end =": ")
print(phrase.index("Mannanikkad"))

#10 Replacing a part of string with another one 10
print("10", end =": ")
print(phrase.replace("Mannanikkad", "Damodaran"))