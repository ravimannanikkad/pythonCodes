# ************************************#
# Writen By Ravi Damodaran           #
# Python class and functions       #
# Working with classes and functions  #
# ************************************#

from student import Student

# Defining 2 Student objects
student1 = Student("Ravi", "Engineering", 3.2)
student2 = Student("Appu", "Accounts", 3.9)

# Checking if they have a good GPA
print(student1.name + "'s status of honor is ",end="")
print(student1.on_honor_roll())
print(student2.name + "'s status of honor is ",end="")
print(student2.on_honor_roll())