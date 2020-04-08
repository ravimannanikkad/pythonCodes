# ************************************#
# Writen By Ravi Damodaran           #
# Python Try and Exception           #
# Working with Try and Exception     #
# ************************************#

# Try is a snippet of code ries to execute and when there
# is an error occures it catches in the Except. Later the
# code executes without problem
try:
    number = int(input("Enter Number"))
    print(number)
except ValueError as err:
    print(err)

print("Hello World !")