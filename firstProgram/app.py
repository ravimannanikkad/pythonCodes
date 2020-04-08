
#************************************#
# Writen By Ravi Damodaran           #
# Python 2D list and nested for loop #
# Working with 2D list and nested for loop#
#************************************#

# 2 Dimensional Matrix
number_grid =[
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]
#print 2D array using nested for loop
for row in number_grid:
    for col in row:
        print(col)
# 3 Dimensional Matrix
number_grid2=[
    [[1,2,3],
     [4,5,6],
     [7,8,9]],
    [[11,12,13],
     [14,15,16],
     [17,18,19]],
    [[21,22,23],
     [24,25,26],
     [27,28,29]]
]
#print ED array using nested for loop
for segment in number_grid2:
    for row in segment:
        for col in row:
            print(col)
# 3 Dimensional Matrix
number_grid2=[
    [[1,2,3],
     [4,5,6],
     [7,8,9]],
    [[11,12,13],
     [14,15,16],
     [17,18,19]],
    [[21,22,23],
     [24,25,26],
     [27,28,29]]
]