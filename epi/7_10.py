###
# Problem
###

# Given an IP address without periods:
# 19216811
# Comput all possible IP address.
# ex: 19.21.68.11, and others

###
# Work
###
# allow 0-padded? (Assume yes)
# Maximum length of string?
# Assume valid input? (Assume yes)

def ip_addresses(s, current=None):
  if current is None:
    current = []
  if len(current) == 4 and not s:
    yield ".".join(current)
  # Possible optimization for "we can't get to four elements"
  for i in xrange(1, len(s) + 1):
    if int(s[:i]) <= 255:
      current.append(s[:i])
      for address in ip_addresses(s[i:], current):
        yield address
      current.pop()

# Tests:
for address in ip_addresses("19216811"):
  print address

# Time: 6 minutes

###
# Mistakes / Bugs / Misses
###
# Forgot to add "not s" condition at 20
# Forgot to loop to len(s) + 1. TODO: make card
# Their solution is seriously to have four nested loops? >_<
# I did ask about valid strings. I don't actually agree with their assessment
# that "001" is somehow invalid, but that's up to the interviewer.
