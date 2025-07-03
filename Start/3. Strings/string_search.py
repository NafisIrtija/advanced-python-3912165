# Example file for Advanced Python by Joe Marini


sample_text = "The quick brown fox jumps over the lazy dog."
temp_str = sample_text.lower()
# Using find() to find the first occurrence of a substring
# print("First occurence of 'the': ", temp_str.find("the"))

# Example with optional start and end parameters
# print("First occurence of 'the': ", temp_str.find("the", 5, 36))
# print("First occurence: 'fox'", temp_str.find("fox", 5, 36))
# print("First occurence: 'fax'", temp_str.find("fax", 5, 36))

# Using index() to find the first occurrence of a substring (raises ValueError if not found)
# print("First occurence: 'fox'", temp_str.index("fox"))
# try:
#   print("First occurence: 'fax'", temp_str.index("fax"))
# except ValueError as e:
#   print("Not found: ", e)

# The 'in' operator can be used for Boolean testing:
print("fox" in temp_str)

# Using rfind() to find the last occurrence of a substring
print(temp_str.rfind("fox"))

# Using rindex() to find the last occurrence of a substring (raises ValueError if not found)
print(temp_str.index("fox"))


# The replace() function will find content in the string and replace it
result = sample_text.replace("lazy", "sucky")
print(result)


result = temp_str.replace("the", "no")
print(result)