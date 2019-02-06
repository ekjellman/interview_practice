###
# Problem
###

# Implement a method rand7() using only a rand5() method

###
# Work
###

import random
def rand7():
  while True:
    num = rand5() * 5 + rand5()
    if num >= 21: continue
    return num % 7

# Test
def rand5():  # Reference implementation
  return random.randint(0, 4)

counts = [0] * 7
for i in xrange(1000000):
  counts[rand7()] += 1
print counts

# Time: 5 minutes

###
# Mistakes / Bugs / Misses
###
# I got lazy and didn't write questions. >_< They would be something like:
# -- Do we want the numbers to be evenly distributed? (Assume yes)
# -- Do we value simpler code over a high level of optimization of rand5()
#    calls? (assume yes)
# -- Do we want to worry about extensibility? (Assume no)

