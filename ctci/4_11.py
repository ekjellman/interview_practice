###
# Problem
###

# You are implementing a binary tree class with, in addition to
# insert, find, and delete methods, has a get_random_node() method
# which gets a random node where each node should be chosen with
# equal probability. Implement get_random_node, and explain implementing
# the other methods

###
# Work
###
# Questions:
# get_random_node() is an object method? (Assume yes)
# I can fully control the implementation of the other methods? (Assume yes)
# output of get_random_node()? (Assume the node object)
# Is the tree meant to be balanced?

# find could be implemented as normal (it doesn't say it's a BST, just a
#   binary tree, so that's probably traversing the whoel tree)
# I would add a "size" object variable. When we insert or delete we would update
#   size on all the appropriate nodes (the parents of the node that gets added)
#   Then, to get a random element, we would generate a random number from 1 to
#   size. For a 1, we return the root. For 2 to left_size + 1, we'd recurse left
#   and otherwise we're recurse right. For example:
#         x
#        / \
#     (10)  (20)
# Here size is 31. If we roll a 1, we return x. If we roll 2-11, we go left
# and if we roll 12-31 we go right.

# For testing purposes, we'll just check the size of the tree when asked, to
# avoid implementing the whole thing.

# I did not implement this, but you could use slightly fewer random numbers by
# generating the random number once, and finding the nth node in the tree by
# similar methods. i.e.: If you roll a 17, you then get the 6th node in right.

import random

class RandomTree(object):
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def __len__(self):
    length = 1
    if self.left: length += len(self.left)
    if self.right: length += len(self.right)
    return length

  def get_random_node(self):
    node_index = random.randint(1, len(self))
    if node_index == 1: return self
    left_length = len(self.left)
    if node_index <= 1 + left_length:
      return self.left.get_random_node()
    return self.right.get_random_node()

a = RandomTree(1)
a.left = RandomTree(2)
a.right = RandomTree(3)
a.right.right = RandomTree(4)
a.right.left = RandomTree(5)
a.left.left = RandomTree(6)

print "6", len(a)

import collections
c = collections.Counter(a.get_random_node() for _ in xrange(10000))
print c

# Time: 21 minutes

###
# Mistakes / Bugs / Misses
###
# Put a colon on the end of line 72

