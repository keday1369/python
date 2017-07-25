# Assignment 4:
#
#   Problems in this assignment are based on the information from this page:
#       http://www.python-course.eu/python3_list_manipulation.php
#
#   1. Create a new branch in PyCharm with name assignment04
#   2. Write python code corresponding to the problems below.
#   3. Use PyCharm to add, commit, and push your changes into your git branch.
#   4. Go to github.com and create a 'Pull Request' for the 'assignment04' branch, and assign it to 'mtday'
#

# Problem 1: Create a variable called "letters" that is an empty list.
letters = []

# Problem 2: Use the list functions (pop, append, extend, insert, remove, index) to add the string "B" to your list,
# and print the result. The output should be:   ['B']
letters.append("B")
print(letters)

# Problem 3: Use the list functions (pop, append, extend, insert, remove, index) to add the string "A" to the beginning
# of the list and print the result. The output should be:   ['A', 'B']
letters.insert(0, "A")
print(letters)

# Problem 4: Use the list functions (pop, append, extend, insert, remove, index) to add the string "C" to the end
# of the list and print the result. The output should be:   ['A', 'B', 'C']
letters.append("C")
print(letters)

# Problem 5: Use the list functions (pop, append, extend, insert, remove, index) to add the string "Z" in between
# "A" and "B" in the list and then print the list. The output should be:   ['A', 'Z', 'B', 'C']
letters.insert(1, "Z")
print(letters)

# Problem 6: Use the list functions (pop, append, extend, insert, remove, index) to add the strings "D", "E", and "F"
# to the end of the list using a single function call, then print the list. The output should be:
#    ['A', 'Z', 'B', 'C', 'D', 'E', 'F']
letters.extend(["D", "E", "F"])
print(letters)

# Problem 7: Use the list functions (pop, append, extend, insert, remove, index) to remove the string "Z" from the
# list, then print the list. The output should be:   ['A', 'B', 'C', 'D', 'E', 'F']
letters.remove("Z")
print(letters)

# Problem 8: Use the list functions (pop, append, extend, insert, remove, index) to move the last element in the list
# to the beginning of the list, then print the list. The output should be:   ['F', 'A', 'B', 'C', 'D', 'E']
letters.insert(0, letters.pop(-1))
print(letters)

# Problem 9: Print out the length of the list. The output should be:   6
print(len(letters))

# Problem 10: Print out the first element in the list. The output should be:   A
print(letters[0])

# Problem 11: The python documentation (https://docs.python.org/3/tutorial/datastructures.html) indicates that lists
# have a "count" function that returns how many times an element appears in the list. Call the "count" function on
# the list to find out how many "A" values exist in the list and print the result. The output should be:   1
print(letters.count("A"))

# Problem 12: The python documentation (https://docs.python.org/3/tutorial/datastructures.html) indicates that lists
# have a "sort" function that orders the values in the list. Call the "sort" function on the list, then print the list.
# The output should be:   ['A', 'B', 'C', 'D', 'E']
letters.sort()
print(letters)

# Problem 13: The python documentation (https://docs.python.org/3/tutorial/datastructures.html) indicates that lists
# have a "clear" function that removes all the values from the list. Call the "clear" function on the list, then print
# the list. The output should be:   []
letters.clear()
print(letters)
