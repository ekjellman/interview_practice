###
# Problem
###

# Given a list of people with birth and death years, find the year with most
# people alive. Count a person's birth and death years as being alive during
# that year. Assume all people were born between 1900 and 2000

###
# Work
###
# Questions:
# How many people?
# How long do people live? (Assume normal life spans)
# What is the current year? (Assume 2019)
# What should we do if there are no people? (None is fine)
# What if there are ties? (Assume any tied year is fine)

# Approaches:
# 1) Turn each person into two items, (start <year>) and (end <year>), sort by
#    year, and count. O(n log n)
# 2) For each year, check if each person is alive. O(ny) (y is number of years
#    to check over
# 3) Make a hashtable (or an array is possibly more optimal, but a little less
#    flexible) and for each person increment the years they were alive by 1.
#    O(nl), where l is the average length of a person's life.

import collections

def highest_pop_year(people):
  # people is a list of (start, end) tuples
  years = collections.defaultdict(int)
  for person in people:
    for year in xrange(person[0], person[1] + 1):
      years[year] += 1
  best_year, best_count = None, 0
  for year in years:
    if years[year] > best_count:
      best_year, best_count = year, years[year]
  return best_year

people = [(1900, 1920), (1910, 1930), (1915, 1935), (1917, 1950)]
print "1917-1920", highest_pop_year(people)

# Time: 10 minutes (FAILED)

###
# Mistakes / Bugs / Misses
###
# There is a fancier way to do that max. Make a card for it.
# Didn't think about "no people" edge case until writing tests.
# had "return best year" for line 40
# I didn't think deeply about whether a n log n solution is better. For most
#   reasonable n, it is better than the O(nl) solution, so I should have gone
#   with it. It would be reasonable to have a discussion of tradeoffs, though.
#   I think this code is easier to understand than the n log n code.
# Did not find the O(n + y) solution.
