# Assignment 5:
#
#   Problems in this assignment are based on the information from this page:
#       http://www.python-course.eu/python3_dictionaries.php
#
#   1. Create a new branch in PyCharm with name assignment05
#   2. Write python code corresponding to the problems below.
#   3. Use PyCharm to add, commit, and push your changes into your git branch.
#   4. Go to github.com and create a 'Pull Request' for the 'assignment05' branch, and assign it to 'mtday'
#

# Problem 1: Create a variable called "letters" that is an empty dictionary.
letters = {}

# Problem 2: Use the update function to add the key/value pair of "A" => 1 to the letters dictionary,
# and print the result. The output should be:   {'A': 1}
letters.update({"A" : 1})
print(letters)

# Problem 3: Use square brackets to add the key/value pair of "B" => 2 to the letters dictionary,
# and print the result. The output should be:   {'A': 1, 'B': 2}
letters["B"] = 2
print(letters)

# Problem 4: Use the update function to change the value of "A" to 3 in the letters dictionary,
# and print the result. The output should be:   {'A': 3, 'B': 2}
letters.update({"A" : 3})
print(letters)

# Problem 5: Use square brackets to change the value of "B" to 4 in the letters dictionary,
# and print the result. The output should be:   {'A': 3, 'B': 4}
letters["B"] = 4
print(letters)

# Problem 6: Retrieve and print the value associated with the key "A" in the dictionary. The output should be:   3
print(letters["A"])

# Problem 7: Create a second dictionary called "more_letters" with these key/value pairs:
#   'X' => 7,  'Y' => 8,  'Z' => 9
more_letters = {"X" : 7, "Y" : 8, "Z" : 9}

# Problem 8: Merge the key/value pairs from "more_letters" into the "letters" dictionary,
# and print the result. The output should be:   {'A': 3, 'B': 4, 'X': 7, 'Y': 8, 'Z': 9}
more_letters.update(letters)
print(more_letters)

# Problem 9: Print out the length of the letters dictionary. The output should be:   5
print(len(more_letters))

# Problem 10: Print out the boolean value indicating whether the letters dictionary contains the key "M".
# The output should be:    False
print("M" in more_letters)

# Problem 11: Remove the key/value pair from the letters dictionary with the key "X", and print the resulting
# dictionary. The output should be:   {'A': 3, 'B': 4, 'Y': 8, 'Z': 9}
del more_letters["X"]
print(more_letters)

# Problem 12: Remove all key/value pairs from the letters dictionary, and print the resulting dictionary.
# The output should be:   {}
more_letters.clear()
print(more_letters)
