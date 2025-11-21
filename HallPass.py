# What you're doing
# You’re making a mini program that checks which students are out of class, how long they’ve been gone, and whether they should be OK, WARNING, or FLAGGED.


# What you need to do (simple version)
# 1. Make 2 lists


# List #1 → student names
names = ['Josiah', 'Luis', 'anothony', 'jamie', 'mari', 'Evins']



# List #2 → minutes they’ve been gone
minutes = [3, 12, 7, 7, 3, 12]  

# The positions must match (name at index 0 matches minutes at index 0)

print(f"{'Index':<6} {'Name':<10} {'Minutes Out':<12} {'Status':<10} {'Notes'}")
print("-" * 50)

# 2. Loop through each student

for i in range(len(names)):
    name = names[i]
    time_out = minutes[i]
    notes = ""


# Go through each student using a loop and check how long they’ve been gone.
    if time_out < 10 or names.count(name) > 1:
        status = "FLAGGED"
    elif time_out <= 5:
        status = "OK"
    else:
        status = "WARNING"

# 4. Add the special rule
# A student is FLAGGED if:
if time_out > 10 or names.count(name) > 1:
        status = "FLAGGED"


# they’ve been out more than 10 minutes OR
 

# their name appears twice (meaning they left class twice)



# 5. Print a report
# For each student, print:


# Name

print(name)
print(status)
print(notes)
print()



# That’s it.
# Make the lists → loop → check rules → print results.