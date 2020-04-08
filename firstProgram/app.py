#*********************************#
# Writen By Ravi Damodaran #
# Python If statements Tutorial
# Working with If statement #
#*********************************#


#########################################
# Basics of python if and else stements#
#########################################
is_male =False
is_tall=True

#if statement with one condition
if is_male :
    print("You are a male ")
else:
    print("You are not a male ")


#If statement with 2 conditions OR
if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You are neither male nor tall ")

#If statement with 2 conditions AND
if is_male and is_tall:
    print("You are a male and tall ")
else:
    print("You are either male or tall,but not both ")

#If statement with 2 conditions and elif
if is_male and is_tall:
    print("You are a male and tall ")
elif is_male and not (is_tall):
    print("You are a short male")
elif not (is_male) and is_tall:
    print("You are not a male but tall")
else:
    print("You are not male not tall ")

####################################
# Comparison inside if statements  #
####################################

# A function to check the largest number
def max_num(num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >=num3:
        return num2
    else:
        return num3
#Print the largest number
print("The largest number among the numebers 4,5,6 is:", end=" ")
print(max_num(4,5,6))
