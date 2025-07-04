# Example file for Advanced Python by Joe Marini
# Itertools: chain, chain.from_iterable

import itertools


# chain() creates a single iterable from multiple
x = itertools.chain("abcd", "1234")
# print(list(x))


# make a prepend function
def prepend(val, iterable):
  return itertools.chain([val],iterable)

# print(list(prepend("a", "bcd")))

# chain.from_iterable is an alternate usage of chain
s1 = "ABCDEFG"
s2 = [1,2,3,4,5]
s3 = ['$','%','@','&']

result = itertools.chain.from_iterable([s1,s2,s3])
print(list(result))