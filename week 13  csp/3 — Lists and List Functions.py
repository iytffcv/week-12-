# # Objective:
# # Students will understand how to create, modify, and access elements in Python lists.

# # Topics Covered:
# # Creating lists, indexing, slicing, appending, popping, sorting, reversing.

# # Examples:

# my_list = ['apple', 'banana', 'cherry']
# print(my_list[0])         # apple
# print(my_list[1:])        # ['banana', 'cherry']

# my_list.append('grape')
# print(my_list)

# my_list.pop(1)
# print(my_list)

# numbers = [3, 1, 4, 2]
# numbers.sort()
# print(numbers)


# # Practice Problems:

# # Create a list with 5 of your favorite foods.

# # Print the second and last item.

# # Add a new item using .append().

# # Remove the first item using .pop(0).

# # Reverse your list using .reverse().

# # Create a list of 3 lists (matrix), and access the middle element. 

# A list is an ordered, mutable collection
fruits = ["apple", "banana", "cherry"]
print("List:", fruits)

# Accessing by index
print("First fruit:", fruits[0])   # apple
print("Last fruit:", fruits[-1])   # cherry

# Modifying a list
fruits.append("grape")
print("After append:", fruits)

fruits.pop(1)  # remove "banana"
print("After pop:", fruits)

# --- Tuples ---

# A tuple is similar to a list, but it's immutable
colors = ("red", "green", "blue")
print("Tuple:", colors)

# You can't modify a tuple, but you can access elements
print("First color:", colors[0])

# Trying to change will result in an error:
# colors[ ] = "yellow"  # Uncommenting this line will cause a TypeError

# --- Sets ---

# A set is an unordered collection of unique elements
numbers = {1, 2, 3, 2, 1}
print("Set:", numbers)  # duplicates removed

# You can add or remove items in a set
numbers.add(4)
print("After add:", numbers)

numbers.remove(2)
print("After remove:", numbers)

# Check membership
print("Is 3 in set?", 3 in numbers)

# --- Converting Between Them ---

# List -> Tuple
fruits_tuple = tuple(fruits)
print("Fruits as tuple:", fruits_tuple) 

# Tuple -> List
colors_list = list(colors)
print("Colors as list:", colors_list)

# List -> Set (to remove duplicates)
dup_list = [1, 2, 2, 3, 3, 3]
unique_set = set(dup_list)
print("Unique elements:", unique_set)


# Create a 2D list (matrix) — for example, 3x4 grid
rows = 3
cols = 4
matrix = [[0 for _ in range(cols)] for _ in range(rows)]

# Print the empty matrix
print("Initial matrix:")
for row in matrix:
    print(row)

# Set some values
matrix[0][0] = 1
matrix[1][2] = 5
matrix[2][3] = 9

# Print updated matrix
print("\nUpdated matrix:")
for row in matrix:
    print(row)

# Iterate through the matrix and do something
print("\nSum of all elements:")
total = 0
for row in matrix:
    for val in row:
        total += val
print(total)

# Transpose the matrix (rows become columns)
transpose = [[matrix[r][c] for r in range(rows)] for c in range(cols)]

print("\nTransposed matrix:")
for row in transpose:
    print(row)
    