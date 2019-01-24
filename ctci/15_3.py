###
# Problem
###

# Implement a simulation of dining philosopers that prevents deadlocks

###
# Work
###

# I need to practice threading in Python.

# There are two easy solutions that I'm aware of: Assign numbers to the
# chopsticks and pick them up in a specific order, or pick them up in whatever
# order and then put them down after a random amount of time if they didn't
# pick up the other chopstick.

# I don't know enough about threading primitives in Python to solve this off the
# top of my head, so I will have to fail it.

# I can make a kind of psuedocodey solution, though.

import random

class Philosopher(object):
  def __init__(self, left, right, num):
    # The two chopstick objects
    self.left = left
    self.right = right
    # An identifier for print messages
    self.num = num

  def eat(self):
    while True:
      left_chop = get_chopstick(self.left)
      right_chop = get_chopstick(self.right)
      if left_chop and right_chop:
        print "Philosopher %d eats" % num
        release_chopstick(self.left)
        release_chopstick(self.right)
        return
      else:
        release_chopstick(self.left)
        release_chopstick(self.right)

  def release_chopstick(chopstick):
    if not chopstick: return
    chopstick.release()

  def get_chopstick(chopstick):
    # Try for some amount of time, at random to avoid synchronicity
    result = chopstick.get_lock(random.randint(100, 1000) / 1000.0)
    if not result: return False
    return True

# Time: 13 minutes (FAILED)

###
# Mistakes / Bugs / Misses
###
# TODO: Make an actual solution to this in Python, make it a card.
# TODO: Also consider implementing the non-random solution
