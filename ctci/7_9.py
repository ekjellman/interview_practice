###
# Problem
###

# Implement a CircularArray.

###
# Work
###
# Questions:
# Use cases, number of elements, etc
# Do we care about efficient insert? (Assume no)

# I don't remember the iterator interface, so I'll implement with a fake name

class CircularList(object):
  def __init__(self):
    self._list = []
    self.rotation = 0

  def rotate(self, amount):
    self.rotation += amount
    self.rotation %= len(self._list)

  def append(self, value):
    self._list.insert(self.rotation, value)
    self.rotation += 1

  def list_copy(self):
    return self._list[self.rotation:] + self._list[:self.rotation]

a = CircularList()
a.append(1)
a.append(2)
a.append(3)
a.append(4)
a.append(5)
print a.list_copy()
a.rotate(2)
print a.list_copy()
a.append(6)
a.append(7)
a.append(8)
print a.list_copy()
a.rotate(2)
print a.list_copy()
a.append(9)
a.append(10)
a.append(11)
print a.list_copy()

# Time:

###
# Mistakes / Bugs / Misses
###
# Did not remember the iterator interface.
# Got insert wrong. Also did not remember if you could insert at the end using
#   len(list)
# Also got order of insert arguments wrong
# REDO
# Before redoing: Make some iterators and cards for that and the insert question

