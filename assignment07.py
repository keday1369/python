# Assignment 7:
#
#   Problems in this assignment are based on the information from this page:
#       http://www.python-course.eu/python3_conditional_statements.php
#
#   1. Create a new branch in PyCharm with name assignment07
#   2. Write python code corresponding to the problems below.
#   3. Use PyCharm to add, commit, and push your changes into your git branch.
#   4. Go to github.com and create a 'Pull Request' for the 'assignment07' branch, and assign it to 'mtday'
#

# Problem 1: Create a boolean variable called "a" with a true value.
a = True

# Problem 2: Create a boolean variable called "b" with a false value.
b = False

# Problem 3: Write an "if" statement that prints "Yes" if "a" is true. The output should be:   Yes
if a == True:
    print("Yes")

# Problem 4: Write an "if" statement that prints "Yes" if either "a" or "b" are true. The output should be:   Yes
if a == True or b == True:
    print("Yes")

# Problem 5: Write an "if" statement that prints "Yes" if "a" is true and "b" is not true. The output should be:   Yes
if a == True and b != True:
    print("Yes")

# Problem 6: Write an "if/else" statement that prints "Yes" if "b" is true and "No" if "b" is false.
# The output should be:   No
if b == True:
    print("Yes")
else:
    print("No")

# Problem 7: Create a variable called "num" with a value of 10.
num = 10

# Problem 8: Write an "if/elif/else" statement that prints "Small" if "num" is less than 5, "Medium" if "num" is 5
# through 10, and "Large" if "num" is greater than 10. The output should be:    Medium
if num < 5:
    print("Small")
elif num < 10:
    print("Large")
else:
    print("Medium")

# Problem 9: Create a variable "max" initialized to -1 if "num" is less than 100 and 1 if "num" is greater than or
# equal to 100.
if num < 100:
    max = -1
if num <= 100:
    max = 1
