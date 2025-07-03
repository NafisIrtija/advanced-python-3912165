# Example file for Advanced Python by Joe Marini
# Sequences and slicing

from collections import deque

names = ["Jim", "Pam", "Creed", "Michael", "Dwight", "Oscar", "Kevin", "Phyllis"]

# a slice is a subset of a sequence. The form is [start:stop:step]

print(names[1:5])
# using a step 
print(names[1:5:2])

# shorthand
print(names[:-1])

# reversing with step of -1
print(names[::-1])

# assigning sequences
new_names = ["Dingle", "Bottle", "Gloop"]
names[0:2] = new_names
print(names)
# the del operator works with slices
del names[0:2]
print(names)
a = names
b = names[:]
names[0] = "Gulg"
print(a)
print(b)
# not all sequence types support slicing, however
deque_names = deque(["Jim", "Pam", "Creed", "Michael", "Dwight", "Oscar", "Kevin", "Phyllis"])
print(deque_names[0])

