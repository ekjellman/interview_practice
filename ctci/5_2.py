###
# Problem
###

# Given a real number between 0 and 1 passed as a double, print the binary
# representation. If the number cannot be represented accurately in 32
# characters, print "ERROR"

###
# Work
###
# Questions:
# Print or return? (assume print)
# Does the 32 characters include the "0."? (Assume yes)

def print_binary_repr(num):
  assert 0 <= num < 1
  rep = ["0", "."]
  while num != 0.0 and len(rep) <= 32:
    num *= 2
    if num >= 1.0:
      rep.append("1")
      num -= 1.0
    else:
      rep.append("0")
  if len(rep) <= 32:
    print "".join(rep)
  else:
    print "ERROR"

print_binary_repr(.875)
print_binary_repr(.03)
print_binary_repr(.0000000000000000000003)
print_binary_repr(.625)

# Time: 5 minutes

###
# Mistakes / Bugs / Misses
###
# It is probably more efficient to print ERROR immediately when len(rep) > 32.
# This works because eventually num becomes 0.0 due to double precision, but it
# is less efficient.
