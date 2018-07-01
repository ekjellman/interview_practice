###
# Problem
###

# Check if a string is a rotation of another string
# i.e. "waterbottle" "erbottlewat" -> True

###
# Work
###

# Questions
# Is O(n) space ok? (Assume yes)
# Case-sensitive? (Assume yes)
# What characters? (Assume any ASCII)
# Empty string?

def is_rotation(a, b):
  return a in b + b

tests = [("waterbottle", "erbottlewat", True),
         ("12345", "23451", True),
         ("12345", "51234", True),
         ("12345", "12345", True),
         ("12345", "34513", False),
         ("", "", True)]

for a, b, expected in tests:
  print a, b, expected, is_rotation(a, b)

# Time: 6 minutes

###
# Mistakes / Bugs / Misses
###

# None
