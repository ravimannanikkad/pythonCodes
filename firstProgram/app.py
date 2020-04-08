
#***************************#
# Writen By Ravi Damodaran  #
# Python Dictionary Tutorial#
# Working with Dictionary   #
#***************************#


monthConversions = {
    #Key : Value
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}
# Method 1 to get value from dictionary
print("Get the value of Oct", end= ":= ")
print(monthConversions["Oct"])

# Method 2 to get value from dictionary
print("Get the value of Mar", end= ":= ")
print(monthConversions.get("Mar","Not a valid Key"))

# Method 2 to get value from dictionary when there is not that value is present
print("Get the value of Ravi", end= ":= ")
print(monthConversions.get("Ravi","Not a valid Key"))
