###
# Problem
###

# Write a program that takes an integer argument and returns all the primes
# between 1 and that number. For example, if your input is 18, return
# [2, 3, 5, 7, 11, 13, 17]

###
# Work
###
# Questions:
# Range of n? (Am I going to use a sieve or enumerate them one at a time?)
# (I'm going to do one at a time)
# Use a generator? (Assume yes)
# Do I need to be 100% sure they're prime? (There are randomized methods for
# determining if something is prime with some probability)

# If I were doing this for real, I would definitely use a library. I think
# gmpy has a is_prime or is_probably_prime method.

def enumerate_primes(n):
  # TODO: Error check n
  for i in xrange(2, n + 1):
    for factor in xrange(2, int(i**.5 + 1.5)):
      if i % factor == 0:
        break
    else:
      yield i

# Test:
for i in enumerate_primes(100):
  print i

# Time: 6 minutes

###
# Mistakes / Bugs / Misses
###
# My original range on line 25 excluded 2 as a prime
# I did discuss the sieving approach, which I discarded due to space concerns.
