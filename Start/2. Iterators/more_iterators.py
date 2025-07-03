# Example file for Advanced Python by Joe Marini
import itertools

# define a list of days in English and French
days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
daysFr = ["Dim", "Lun", "Mar", "Mer", "Jeu", "Ven", "Sam"]

# the enumerate function
# for i, day in enumerate(days,start=1):
#   card = f"{i}th"
#   if i == 1:
#     card = "1st"
#   elif i==2:
#     card = "2nd"
#   elif i==3:
#     card = "3rd"
#   print(f"The {card} day is {day}")

# use zip to combine sequences
# for i, d in enumerate(zip(days, daysFr),start=1):
  # for i, day in enumerate(days,start=1):
#   card = f"{i}th"
#   if i == 1:
#     card = "1st"
#   elif i==2:
#     card = "2nd"
#   elif i==3:
#     card = "3rd"
  # print(f"{i}, {d[0]}, {d[1]}")
  # print(i,d)

# use enumerate and zip together


# use zip_longest
seq1 = ["A","B","C","D","E","F"]
seq2 = [1, 2, 3, 4]
seq3 = "xyz"
    
for x in itertools.zip_longest(seq1, seq2, seq3, fillvalue=":o"):
  print(x)