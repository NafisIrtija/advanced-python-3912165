# Example file for Advanced Python by Joe Marini
# Itertools: count, cycle, accumulate


import itertools

names = ["Joe", "Jane", "Jim"]

# cycle iterator can be used to cycle over a collection infinitely
cc = itertools.cycle(names)
# for i in range(20):
#   print(next(cc))


# use count to create a simple counter
counter = itertools.count(100, 10)
# for i in range(20):
#   print(next(counter))


# accumulate creates an iterator that accumulates values
vals = [10,20,30,40,50,40,30]
acc = itertools.accumulate(vals, max)
# print(list(acc))


# amortize a loan over a set number of payments for a 2000 loan at 4%
payments = [100, 125, 200, 105, 100, 120, 110, 130, 150, 100, 110, 120]
update = lambda balance, payment: round(balance * 1.04) - payment
balances = list(itertools.accumulate(payments, update, initial=2000))
print(balances)