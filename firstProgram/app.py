# ************************************#
# Writen By Ravi Damodaran           #
# Python File Operations        #
# Working with file Operations   #
# ************************************#

employee_file=open("employee.txt", "r")

for i in employee_file.readlines():
    print(i)

employee_file.close()

employee_file =open("employee.txt", "w")
employee_file.write("\nAppu idiont - CEO")
employee_file.close()