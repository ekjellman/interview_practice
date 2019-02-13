###
# Problem
###

# A masseuse gets a sequence of back-to-back appointments, but needs a 15 minute
# break between them and so can't accept adjacent requests. Find the optimal
# number of minutes she can book.

###
# Work
###
# Questions:
# Extensibility? (Assume it doesn't matter)
# -- MInutes needed for break, etc
# -- Wanting to return appointments instead of total minutes
# Number of entries given?
# -- Straight recursive code might be easier to understand

def masseuse_brute(entries):
  if not entries:
    return 0
  return max(entries[0] + masseuse_brute(entries[2:]),
             masseuse_brute(entries[1:]))

# Test
print masseuse_brute([30, 15, 60, 75, 45, 15, 15, 45]), 180

def masseuse_memo(entries, index=0, cache=None):
  if index >= len(entries):
    return 0
  if cache is None:
    cache = {}
  if index in cache:
    return cache[index]
  take_appointment = entries[index] + masseuse_memo(entries, index+2, cache)
  pass_appointment = masseuse_memo(entries, index+1, cache)
  result = max(take_appointment, pass_appointment)
  cache[index] = result
  return result

print masseuse_memo([30, 15, 60, 75, 45, 15, 15, 45]), 180
print masseuse_memo([]), 0
print masseuse_memo([60, 90]), 90

def masseuse_dp(entries):
  if len(entries) == 0: return 0
  if len(entries) == 1: return entries[0]
  table = [0] * len(entries)
  table[-1] = entries[-1]
  table[-2] = max(entries[-1], entries[-2])
  for i in xrange(len(table) - 3, -1, -1):
    take_app = entries[i] + table[i+2]
    pass_app = table[i+1]
    table[i] = max(take_app, pass_app)
  return table[0]

print masseuse_dp([30, 15, 60, 75, 45, 15, 15, 45]), 180
print masseuse_dp([]), 0
print masseuse_dp([60, 90]), 90
print masseuse_dp([60]), 60

# Time: 17 minutes

###
# Mistakes / Bugs / Misses
###
# Wasn't sure if entries[2:] would work for a list of 1 entry. TODO: card
# Her solution of making the DP table two longer is interesting, and I should
# keep it in mind.
# Did not consider solution that didn't keep the whole table. TODO: card
