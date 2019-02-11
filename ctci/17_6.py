###
# Problem
###

# Write a method to count the number of 2s between 0 and n

###
# Work
###
# Questions:
# The number of digit 2s? So the number "222" counts as 3 2s? (Assume yes)
# Maximum n?
# Only counting integers? ;-)
# Positive n? (assuming yes. Could easily add negatives with abs)
# Input and output both ints?

def two_count_brute(n):
  count = 0
  for i in xrange(n + 1):
    s = str(i)
    count += s.count("2")
  return count

# Tests:
print two_count_brute(10), 1
print two_count_brute(100), 20
print two_count_brute(250), 106
print two_count_brute(226), 77

def two_count(n):
  count = 0
  multiplier = 1
  discard = 0
  while n > 0:
    digit = n % 10
    multiples = n / 10
    this_count = multiples * multiplier
    if digit == 2:
      this_count += (discard + 1)
    elif digit > 2:
      this_count += multiplier
    discard += digit * multiplier
    multiplier *= 10
    count += this_count
    print this_count
    n /= 10
  return count

print two_count(10), 1
print two_count(100), 20
print two_count(250), 106
print two_count(226), 77
print two_count(526221), two_count_brute(526221)

# Time: 21 minutes

###
# Mistakes / Bugs / Misses
###
# Forgot to add 1 to the discard in line 39
# Forgot to divide n by 10 each time through the loop
# Flailed a little bit figuring out the exact algorithm. >_<
