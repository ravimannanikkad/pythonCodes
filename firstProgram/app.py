#*********************************#
# Writen By Ravi Damodaran #
# Python Calculator Tutorial
# Working with Advanced Calculator #
#*********************************#


num1 = float(input("Enter First Number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second Number: "))

# Check for operator and do the operation
if op == "+":
    print(str(num1)+" "+ op +" "+ str(num2)+ "=", end= " ")
    print(num1+num2)
elif op == "-":
    print(str(num1) + " " + op + " " + str(num2) + "=", end=" ")
    print(num1-num2)
elif op == "*":
    print(str(num1) + " " + op + " " + str(num2) + "=", end=" ")
    print(num1 * num2)
elif op == "/":
    print(str(num1) + " " + op + " " + str(num2) + "=", end=" ")
    print(num1 / num2)
elif op == "%":
    print(str(num1) + " " + op + " " + str(num2) + "=", end=" ")
    print(num1 % num2)
else:
    print("Invalid Operation")
