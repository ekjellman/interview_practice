###
# Problem
###

# For a given n, print all valid combinations of n pairs of parens.
# Such as ((())) or (()())

###
# Work
###

# Questions:
# Size of n
# Print / generator / return / etc
# What to do for n = 0? (Assume print nothing)
# What to do for negative n (Assume print nothing)

def gen_parens(n, count=0):
  if n == 0 and count == 0:
    yield ""
  if n < 0:
    raise StopIteration
  for p in gen_parens(n-1, count+1):
    yield "(" + p
  if count > 0:
    for p in gen_parens(n, count-1):
      yield ")" + p

# Test
for p in gen_parens(3):
  print p

for i in xrange(10):
  print i, len(list(gen_parens(i)))

# Time: 7 minutes

###
# Mistakes / Bugs / Misses
###
# None?
