# Example file for Advanced Python by Joe Marini
# Demonstrate how to use dictionary comprehensions

# define a list of temperature values
ctemps = [0, 12, 34, 100]

# Use a comprehension to build a dictionary
temp_dict = {c: c * 9 / 5 + 32 for c in ctemps}
# print(temp_dict)

# Merge two dictionaries with a comprehension
team1 = {"Jones": 24, "Jameson": 18, "Smith": 58, "Burns": 7}
team2 = {"White": 12, "Macke": 88, "Perce": 4}

team = {x : y for item in (team1,team2) for x,y in item.items()}
print(team)
teamm = {**team1, **team2}
print(teamm)