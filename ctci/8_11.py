###
# Problem
###

# Find the number of ways to give change for n cent using quarters, dimes,
# nickels, and pennies.

###
# Work
###

# Questions:
# Range of n
# Do we want to be flexible about the coins we might use to give change?
#   -- i.e., other kinds of coins
# Use cases
# Do we want the actual ways, or just the number of ways? (assuming number)
# Assuming a solution that returns the same set of coins is unique.
#  -- i.e. (penny, penny, nickel) is the same as (penny, nickel, penny)
# Invalid input?

def ways(coins, n, next_coin=0, cache=None):
  if cache is None:
    cache = {}
  if (n, next_coin) in cache:
    return cache[(n, next_coin)]
  if n == 0: return 1
  if next_coin == len(coins) - 1: return 1 if n % coins[-1] == 0 else 0
  total_ways = 0
  for next_n in xrange(n, -1, -coins[next_coin]):
    total_ways += ways(coins, next_n, next_coin + 1, cache)
  cache[(n, next_coin)] = total_ways
  return total_ways

# Tests
print "1", ways([25, 10, 5, 1], 0)
print "1", ways([25, 10, 5, 1], 3)
print "2", ways([25, 10, 5, 1], 5)
print "4", ways([25, 10, 5, 1], 11)
print "13", ways([25, 10, 5, 1], 25)
print "0", ways([25, 10, 5, 1], -1)
print "0", ways([3, 6], 1)
print "?", ways([25, 10, 5, 1], 10000)


# Time: 22 minutes

###
# Mistakes / Bugs / Misses
###
# Did not ask about invalid input before starting tests
# Changed case at 28 after testing for speed. Was
#  if next_coin == len(coins): return 0
# Misunderstood the time complexity of the solution. Since generating each
# entry takes O(n) effort, and there are O(nc) entries, the time complexity
# is O(n**2 * c), which still makes larger values of n difficult to calculate.
