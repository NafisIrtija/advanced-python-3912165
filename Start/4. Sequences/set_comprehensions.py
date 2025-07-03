# Example file for Advanced Python by Joe Marini
# Demonstrate how to use set comprehensions

# define a list of temperature data points
ctemps = [5, 10, 12, 14, 10, 23, 41, 30, 12, 24, 12, 18, 29]

# build a set of unique Fahrenheit temperatures
temps = [x * 9 / 5 + 32 for x in ctemps]
print(temps)
utemps = {x * 9 / 5 + 32 for x in ctemps}
print(utemps)

# build a set from an input source
sTemp = "The quick brown fox jumped over the lazy dog"
chars = {c.upper() for c in sTemp}
print(''.join(chars))