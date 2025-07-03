# Example file for Advanced Python by Joe Marini
# Itertools: combinations and permutations

import itertools


# product() produces the cartesian product of input iterables
cards = "A23456789TJQK"
suits = "SCHD"

deck = list(itertools.product(cards, suits))
# print(len(deck))
# for card in deck:
#   print(f"{card[0]} of {card[1]}")
# permutations() creates tuples of a given length with no repeated elements
teams = ("A","B","C","D")
result =list(itertools.permutations(teams, 2))
# for t in result:
#   print(''.join(t))

# combinations() will create combinations of a given length with no repeats
team_combo = list(itertools.combinations(teams,3))
# for t in team_combo:
#   print(''.join(t))
print(team_combo)
# combinations_with_replacement() will create combinations of a given length with repeats
team_combo_with_r = list(itertools.combinations_with_replacement(teams,3))
# for t in team_combo_with_r:
#   print(''.join(t))
print(team_combo_with_r)
