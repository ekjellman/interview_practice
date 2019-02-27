###
# Problem
###

# See 6_7, but now buying and selling a stock twice. The second buy must be
# made after the first sale.

###
# Work
###
# Questions:
# Size of prices?
# Can we use O(n) space?
# Do we have to buy/sell twice? (assume yes)

def buy_twice(prices):
  # Two approaches:
  # Make a pass to get all the best answers for one sale, then a second pass
  # using that list
  # Or, just do a double loop.
  # I think the first approach is cleaner but takes O(n) space, so we'll do the
  # second.
  if len(prices) <= 3: return None
  best_first_buy = prices[0]
  best_first_profit = float("-inf")
  best_total_profit = float("-inf")
  for i in xrange(1, len(prices) - 2):
    best_first_profit = max(best_first_profit, prices[i] - best_first_buy)
    best_first_buy = min(best_first_buy, prices[i])
    best_second_buy = prices[i + 1]
    best_second_profit = float("-inf")
    for j in xrange(i + 2, len(prices)):
      best_second_profit = max(best_second_profit, prices[j] - best_second_buy)
      best_second_buy = min(best_second_buy, prices[j])
      best_total_profit = max(best_total_profit, best_first_profit + best_second_profit)
  return best_total_profit

# Tests:
print buy_twice([0, 2, 3, 5]), "4"
print buy_twice([310, 315, 275, 295, 260, 270, 290, 230, 255, 250]), "55"
print buy_twice([0, -10, -20, -30, -40, -50]), "-20"
print buy_twice([0, 5, 6, 3, 9, 11, 2, 10, 8, 14]), "23"

# Time: 15 minutes (FAILED)

###
# Mistakes / Bugs / Misses
###
# Forgot a paren on 29
# Had buy instead of profit in the max at 35
# There's an O(n) time solution. Basically, compute and store the first buys
# as noted in my "first" solution. Then, work BACKWARDS finding the best buys
# from that time forward, and compute the intersection.

# For example:
# [12, 11, 13, 9, 12, 8, 14, 13, 15]
# Forward:  [0, 0, 2, 2, 3, 3, 6, 6, 7]
# Backward: [7, 7, 7, 7, 7, 7, 2, 2, 0]
#      Best is the sum here ^
# Make card for algorithm (TODO)
