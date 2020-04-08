# Writen By Ravi Damodaran #
# Python Functions Tutorial
# Working with Functions #

# Simple Function
def say_hi():
    print("Hello User")


# Function with input Parameters
def say_me(name, age):
    print("Hello " + name + ", You are "+ age+ " years old")

def calculate_multiples(num):
    res1=num*num
    res2=res1*num
    #returning 2 results
    return res1 ,res2


# Calling a simple function
say_hi()
# Calling a function with input parameters
say_me("Ravi","31")
# Calling a function with input parameters and receiving value
print("The square of the number 4 is ",end= ": ")
#getting results to two variables
result1,result2 =calculate_multiples(4)
print(result1)
print("The cube of the number 4 is ",end= ": ")
print(result2)