
# Writen By Ravi Damodaran #
# Python Lists Tutorial
# Working with Lists #

#creating a list of friends here
friends =["ammu","Appu","Ramu","June","Mahesh","Ravi","Aravind"]

# printing a list here
print("List of friends",end=": ")
print(friends)

#printing the contents of list using index
print("The friend on index 0",end=": ")
print(friends[0])

#printing the contents of list using negative index
print("The friend on index -1",end=": ")
print(friends[-1])

#printing one part of the contents of list
print("The part of contents in the list from index 1",end=": ")
print(friends[1:])

#printing one portion of the contents of list
print("The portion of contents in the list from index 1 to 4",end=": ")
print(friends[1:4])

#Modifying values inside list
print("Modify value of Appu to Raman")
friends[1]="Raman"
print(friends)