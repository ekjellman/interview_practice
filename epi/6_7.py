###
# Problem
###

# Given a list of stock prices over time, find the maximum profit you could make by
# buying and selling one share of a stock. You must buy before selling.

# Ex:
# [310, 315, 275, 295, 260, 270, 290, 230, 255, 250] -> 30  (260 -> 290)

###
# Work
###
# Do we have to buy/sell at all? (Assume yes)
# size of array

def best_transaction(prices):
  if len(prices) <= 1: return None  # or raise, or 0, or whatever
  lowest_buy = prices[0]
  best = float("-inf")
  for i in xrange(1, len(prices)):
    best = max(prices[i] - lowest_buy, best)
    lowest_buy = min(lowest_buy, prices[i])
  return best

# Tests:
print best_transaction([310, 315, 275, 295, 260, 270, 290, 230, 255, 250]), "30"
print best_transaction([10, 20, 30, 40, 50]), "40"
print best_transaction([-10, -20, -30, -40, -50]), "-10"
print best_transaction([5, 7, 9, 4, 6, 8, 3, 5, 7, 2, 4, 6]), "4"

# Time: 9 minutes

###
# Mistakes / Bugs / Misses
###
# had inf instead of -inf at 20
# Forgot the -1 at 21
