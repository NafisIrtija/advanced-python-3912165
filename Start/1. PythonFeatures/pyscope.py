# Example file for Advanced Python by Joe Marini
# Understanding Python scope


# declare a variable within the global scope
# x = 2

# define a local function with a variable "x"
# def func1():
#   global x
#   x = 10
#   print(x)

# Run the test function and observe the two results
# func1()
# print(x)

# x = x+5
# print(x)
# func1()

# Nested functions create inner scopes. These are called closures:
def multiplier_maker(factor):
  def multiply(num):
    return num * factor
  return multiply

my_mult = multiplier_maker(10)
result = my_mult(12)

print(result)