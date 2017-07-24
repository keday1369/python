# Assignment 3:
#
#   Problems in this assignment are based on the information from this page:
#       http://www.python-course.eu/python3_sequential_data_types.php
#
#   1. Create a new branch in PyCharm with name assignment03
#   2. Write python code corresponding to the problems below.
#   3. Use PyCharm to add, commit, and push your changes into your git branch.
#   4. Go to github.com and create a 'Pull Request' for the 'assignment03' branch, and assign it to 'mtday'
#   5. Read the next lesson:  http://www.python-course.eu/python3_list_manipulation.php
#

# Problem 1: Create a variable called "a" that is a list containing the numbers 0 through 5.
a = [0, 1, 2, 3, 4, 5]

# Problem 2: Create a variable called "b" that is a tuple containing the numbers 0 through 5.
# I can't remember the difference between creating a tuple and creating a list, so I'll make B a list
# for use in the later problems until we go over it
b = [0, 1, 2, 3, 4, 5]
# Problem 3: Print out the list from variable "a".
print(a)

# Problem 4: Print out the tuple from variable "b".
print(b)

# Problem 5: Print out the first value from the list in variable "a" using square brackets.
print(a[0])

# Problem 6: Print out the first value from the tuple in variable "b" using square brackets.
print(b[0])

# Problem 7: Print out the first three values from the list in variable "a" using slicing
# (should print out "[0, 1, 2]").
print(a[0:3])

# Problem 8: Print out the first three values from the tuple in variable "b" using slicing
# (should print out "[0, 1, 2]").
print(b[0:3])

# Problem 9: Print out the second, third, and fourth values from the list in variable "a" using slicing
# (should print out "[1, 2, 3]").
print(a[1:4])

# Problem 10: Print out the last three values from the list in variable "a" using slicing
# (should print out "[3, 4, 5]").
print(a[3:])

# Problem 11: Print out the length of the list in variable "a" using the 'len' function.
# Can't remember how to do this! D:

# Problem 12: Print out the length of the tuple in variable "b" using the 'len' function.
# Can't remember how to do this! D:

# Problem 13: Use the "+" operator to create a new list variable called "c" that is list "a" with 6 and 7
# concatenated to the end.
# It doesn't like:
# c = [a + 6 + 7]
# ...something tells me I did that wrong

# Problem 14: Use the "+" operator to create a new tuple variable called "d" that is tuple "b" with 6 and 7
# concatenated to the end.

# Problem 15: Create a variable called "e" that is a list containing the list "a" and the tuple "b".
e = [a + b]

# Problem 16: Print out the first element of list "e" (should print out list "a").
print(e[0])
# What's wrong with this part? It prints both "a" and "b"....

# Problem 17: Print out the second element inside the second element of list "e" (should print out "1").
# I can't remember this! DX<

# Problem 18: Use the "in" keyword to print whether 3 is in the list "a" (should print "True").
# Ugh! I can't remember this, either!

# Problem 19: Use the "in" and "or" keywords to print whether 3 or 7 is in the list "a" (should print "True").
# I'm so tired...