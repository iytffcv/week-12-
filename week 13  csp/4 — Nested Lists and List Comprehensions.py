


list1= [[1, 2, 3]
print(list1[-1])  #output: 4
list2 = [4, 5, 6]
print(list2[0]  #output: 4
nested_list = [list1, list2]
print(nested_list[0])
print(nested_list[1])
print(nested_list[1][1])
print(nested_list[1][0])

fruits = ["apple" , "orange" , "banana" , "coconut"]
vagetables = ["celery" , "carrots" , "potatoes"]
meats = ["chicken" , "fish" , "turkey"]

groceries = [fruits , vegetables , meats]
print(groceries[2][2])
print(groceries[1][-2]
print(groceries[0][-2]

for collection in groceries:
print(collection)

for collection in groceries:
    for collection in groceries:
        print(food, end=" 
    print()


num_pad = ((1, 2, 3))
          ((4, 5, 6))
          ((7, 8, 9))
          ("*", 0, "#"))
          
for row in num_pad
    for num in row:
        print(num, end"")
     print()

# Objective:
# Students will manipulate nested lists and understand basic list comprehensions.

# Key Notes:

# A list can contain other lists.

# List comprehensions provide a concise way to create lists.

# Examples:Objective:
# Students will manipulate nested lists and understand basic list comprehensions.

# Key Notes:

# A list can contain other lists.

# List comprehensions provide a concise way to create lists.

# Examples:

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0])


print(matrix[2][1])

sum_list = [row[-1] for row in matrix]

print(sum_list)


# Practice Problems:

# Build a matrix variable containing 3 lists of 3 numbers each.

# Print the first list.

# Print the second item from the third list.

# Use a list comprehension to extract the last item from each sub-list.

# Challenge: Create a new list containing squares of numbers from 1–10 using a comprehension.
squares = [x**2 for x in range (1, 11)]

print(squares)