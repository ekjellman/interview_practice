###
# Problem
###

# Replace all spaces in a string with "%20". You can assume the string has
# enough space at the end to hold the additional characters

###
# Work
###

# Questions:
# This is Python, so should I assume a list of characters instead of a string?
# Only ASCII 32, or whatever it is?
# Do I have to verify either of the lengths, particularly the character array
#   length?

# Actual string solution
def URLify(s):
  return s.replace(" ", "%20")

# List of chars solutions. Modifies string_list in place
def URLify_list(string_list, string_length):
  string_index = string_length - 1
  new_index = len(string_list) - 1
  while string_index >= 0:
    if string_list[string_index] == " ":
      string_list[new_index] = "0"
      string_list[new_index - 1] = "2"
      string_list[new_index - 2] = "%"
      new_index -= 3
    else:
      string_list[new_index] = string_list[string_index]
      new_index -= 1
    string_index -= 1

# Tests:
tests = [("Mr John Smith", "Mr%20John%20Smith"),
         ("test", "test"),
         ("   ", "%20%20%20"),
         ("", "")]

for test in tests:
  input_str, expected = test
  print test, expected == URLify(input_str)

###

for test in tests:
  input_str, expected = test
  spaces = input_str.count(" ")
  input_list = list(input_str) + [" "] * (spaces * 2)
  URLify_list(input_list, len(input_str))
  expected_list = list(expected)
  print test, input_list == expected_list
  print input_list
  print expected_list


# Time: 19 minutes

###
# Mistakes / Bugs / Misses
###

# Line 53: Forgot to pass length of string
# Forgot URLify_list returned nothing, test harness was wrong
# Test harness passed input_list wrong (list elements of ["  "] instead of
#   [" ", " "] for padding
