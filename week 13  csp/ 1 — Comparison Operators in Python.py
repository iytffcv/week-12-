# Objective:
# Students will learn how to compare values using Python’s comparison operators and interpret Boolean results.

# Topics Covered:
# ==, !=, >, <, >=, <=

# Key Notes:

# Comparison operators compare two values and return either True or False.

# Remember: = is assignment, while == is comparison.

a = 3
b = 4

print(a == b)   # False
print(a != b)   # True
print(a > b)    # False
print(a < b)    # True
print(a >= b)   # False
print(a <= b)   # True


#predict the output of the following comparisons:
10 > 5 #TRUE
7 == 2 * 3 + 1 #TRUE 
8 != 8 #FLASE
4 <= 2 + 2 #True

# Write 3 examples that result in True and 3 that result in False.
5 < 10 #TRUE
7 != 9 #TRUE
12 >= 6 * 2 #TRUE
3 == 5 #FALSE
9 < 4 #FALSE
8 != 8 #FLASE
# Create a simple grade-checking condition:
# where a student must check if their score is greater than or equal to 60 to pass a test.
# Ask for the student's score
score = int(input("Enter your score: "))


if score >= 60:
    print("You passed the test! 🎉")
else:
    print("You failed the test. 😢")
# practice problem :
# The password must be at least 8 characters long and contain at least one digit.password = "mypassword1"
