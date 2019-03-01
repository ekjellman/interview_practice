###
# Problem
###

# A palindromic string is a string which, when all non-alphanumeric
# characters are removed, reads the same backwards and forwards ignoring case.

# Implement a function which takes as input a string s and returns true if
# s is a palindromic string.

###
# Work
###
# Questions:
# Length of s
# alphanumeric being a-z A-Z 0-9?
# Unicode? (assume ascii)

import string

def is_palindromic_string(s):
  valid = set(string.ascii_letters + string.digits)
  front = 0
  back = len(s) - 1
  while front < back:
    while front < len(s) and s[front] not in valid:
      front += 1
    while back >= 0 and s[back] not in valid:
      back -= 1
    if back <= front or front >= len(s) or back < 0:
      return True
    if s[front].lower() != s[back].lower():
      return False
    front += 1
    back -= 1
  return True

# Tests
print is_palindromic_string("      "), "True"
print is_palindromic_string("!!!a???"), "True"
print is_palindromic_string("aaa???aaa"), "True"
print is_palindromic_string("aaa??aaa"), "True"
print is_palindromic_string("aaa??baa"), "False"
print is_palindromic_string("Able was I, ere I saw Elba!"), "True"
print is_palindromic_string("Able was I, erf I saw Elba!"), "False"
print is_palindromic_string("A man, a plan, a canal, Panama."), "True"
print is_palindromic_string("A man, a plan, accanal, Panama."), "True"



# Time:

###
# Mistakes / Bugs / Misses
###
# Forgot colon on line 26
# Forgot to import string
# On lines 26 and 28, put the guard conditions last (TODO: make card. You need the bounds checks first)

