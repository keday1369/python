#
# Assignment 11:
#
# Using loops, write code to print out the following tic-tac-toe board:
#
#    0 | 1 | 2
#   ---+---+---
#    3 | 4 | 5
#   ---+---+---
#    6 | 7 | 8
#

row = 1
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8]
number = 0
while row < 4:
    print(" " + str(numbers[number]) + " | " + str(numbers[number + 1]) + " | " + str(numbers[number + 2]))
    if row != 3:
        print("---+---+---")
    number += 3
    row += 1