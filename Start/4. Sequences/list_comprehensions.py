# Example file for Advanced Python by Joe Marini
# Demonstrate how to use list comprehensions


# define two lists of numbers
evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# Perform a mapping and filter function on a list using built-in functions

evenSquared = list(map(lambda x : x * x, evens))
oddSquared = list(map(lambda x : x * x, odds))
print(evenSquared)
print(oddSquared)

result = list(map(lambda x: x * x, filter(lambda y : y > 4 and y < 16, evens)))
print(result)
result = [x * x for x in evens if x > 4 and x < 16]
print(result)
# Derive a new list of numbers from a given list


# Limit the items operated on with a predicate condition
