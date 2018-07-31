import collections

###
# Problem
###

# Design and implement a hash table which uses chaining to handle collisions

###
# Work
###
# Questions:
# What functions do we need? (For now, assume add, get, delete)
# Details about use cases and resizing (We'll assume just normal use for now)
# Built-in hash() function ok? (Assume yes)

class Dummy(object):
  pass

class HashTable(object):
  def __init__(self):
    # Could take in a capacity
    self.lists = [collections.deque() for _ in xrange(10)]
    self.size = 0
    self.capacity = 7  # We'll resize at 70%

  def add(self, key, value):
    self.remove(key)  # No duplicate keys
    bucket = hash(key) % len(self.lists)
    self.lists[bucket].append((key, value))
    self.size += 1
    if self.size > self.capacity:
      self.resize()

  def resize(self):
    new_lists = [collections.deque() for _ in xrange(len(self.lists) * 2)]
    self.capacity *= 2
    for bucket in self.lists:
      for key, value in bucket:
        new_bucket = hash(key) % len(new_lists)
        new_lists[new_bucket].append((key, value))
    self.lists = new_lists

  def remove(self, key):
    bucket = hash(key) % len(self.lists)
    remove_item = None
    for item in self.lists[bucket]:
      if item[0] == key:
        remove_item = item
    if remove_item:
      self.lists[bucket].remove(remove_item)

  def find(self, key):
    bucket = hash(key) % len(self.lists)
    for item in self.lists[bucket]:
      if item[0] == key:
        return item[1]
    return None

import random
ht = HashTable()
reference = {}
for i in xrange(100):
  key = random.randint(0, 100)
  value = random.randint(0, 1000000)
  ht.add(key, value)
  reference[key] = value
for key in reference:
  value = reference[key]
  ht_value = ht.find(key)
  assert value == ht_value
for key in reference.keys():
  del reference[key]
  ht.remove(key)
  for remaining_key in reference:
    value = reference[remaining_key]
    ht_value = ht.find(remaining_key)
    assert value == ht_value

# Time: 29 minutes (REDO)

###
# Mistakes / Bugs / Misses
###
# Line 39 was self.lists[bucket]
# Line 54 was remove(item) instead of remove(remove_item)
