
#************************************#
# Writen By Ravi Damodaran           #
# Python exponent function Tutorial  #
# Working with exponent function     #
#************************************#


# A function to find the exponential of the base number
def rasie_to_power(base_num,power_num):
    result =1
    for index in range(power_num):
        result=result*base_num
    return result

print(rasie_to_power(4,3))

