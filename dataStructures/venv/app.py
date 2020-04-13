# ****************************************************#
# Created By: Ravi Damodaran
# Organization: Vaayoo
# Fibanoci Series and factorial of a number
# ****************************************************#


def generate_factorial(n):
    if n >= 1:
        return n * generate_factorial(n - 1)
    else:
        return 1


def generate_fibanoci(n):
    if n >= 3:
        return generate_fibanoci(n - 1) + generate_fibanoci(n - 2)
    else:
        return 1


num = int(input("Enter the number for fibanoci series"))

print("fibanoci of the number is " + str(generate_fibanoci(num)))
print("factorial of the number is " + str(generate_factorial(num)))
