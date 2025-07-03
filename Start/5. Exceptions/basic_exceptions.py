# Example file for Advanced Python by Joe Marini
# Working with basic exception handling

# Try to execute some code that might cause an exception:
try:
  num = input("Enter the first number: ")
  denom = input("Enter the second numnber: ")
  n = int(num)
  d = int(denom)
  print(n/d)
except ValueError:
  print("Not an acceptable value")
except ZeroDivisionError:
  print("Can't divide by zero!")
except Exception as e:
  print("Something went wrong: ", e)
finally:
  print("Ooh la la!")
