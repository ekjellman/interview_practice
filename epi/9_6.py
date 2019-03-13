###
# Problem
###

# Write recursive and iterative routines to compute the jump-first
# order of a postings list

###
# Work
###
# Questions:
# So if a jump field leads to an already explored node, which next
# field do we explore from first? (Assume the last node we've seen)
# Size of list?

class PostingsList(object):
  def __init__(self, value):
    self.next_node = None
    self.jump = None
    self.value = value

def postings_iterative(node):
  stack = [node]
  order = []
  visited = set()
  while stack:
    current = stack.pop()
    if current in visited: continue
    order.append(current)
    visited.add(current)
    if current.next_node and current.next_node not in visited:
      stack.append(current.next_node)
    if current.jump and current.jump not in visited:
      stack.append(current.jump)
  return order

def postings_recursive(node, visited=None):
  if visited is None:
    visited = set()
  if node is None or node in visited:
    return []
  visited.add(node)
  return ([node] + postings_recursive(node.jump, visited)
                 + postings_recursive(node.next_node, visited))

# Test:
f = postings_recursive   # Or postings iterative
a = PostingsList("a")
b = PostingsList("b")
c = PostingsList("c")
d = PostingsList("d")
a.next_node = b
b.next_node = c
c.next_node = d
d.next_node = None
a.jump = c
b.jump = d
c.jump = b
d.jump = d
order = f(a)
print [x.value for x in order], "a c b d"

a = PostingsList("a")
b = PostingsList("b")
c = PostingsList("c")
d = PostingsList("d")
a.next_node = b
b.next_node = c
c.next_node = d
d.next_node = None
a.jump = c
b.jump = d
c.jump = a
d.jump = b
order = f(a)
print [x.value for x in order], "a c d b"

# Time: 19 minutes (FAILED. Algorithm correct, missed part of problem. See below)

###
# Mistakes / Bugs / Misses
###
# Iterative
# Missed colon on 22
# Forgot to skip current if we've visited it
# when I removed node from {node}, I forgot to change it to a set()
# Recursive
# Forgot to pass visited along
# Big miss: I missed that it said "each node has an integer valued
# field" that holds the order, so I created a visited and order
# list I didn't need.
