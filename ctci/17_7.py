###
# Problem
###
# You have a list of the 10,000 most common baby names, and their frequencies.
# But some of these names have multiple spellings, like Jon and John. So you
# also have a list of pairs of equivalent names. Given the frequencies and
# the pairs of equivalent names, output the true frequencies of each name.
# Name pairs are transitive and symmetric (i.e. if (Jon, John) and
# (John, Johnny), then (Jon, Johnny)

###
# Work
###
# Questions:
# Are our names in the name pairs all in the most common baby names?
#   (If so, I can save a pre-processing step) (Assume yes)
# Output? (Assume dictionary)
# One-off? Might consider a less general solution.

# The bulk of this problem is finding the name groups that are the same. We have
# to use a graph for this, or find a way of merging groups when we encounter
# them.

import collections
def get_name_groups(name_pairs):
  graph = collections.defaultdict(list)
  for a, b in name_pairs:
    graph[a].append(b)
    graph[b].append(a)
  visited = set()
  groups = []
  for name in graph:
    if name in visited: continue
    group = []
    stack = [name]
    while stack:
      current = stack.pop()
      group.append(current)
      visited.add(current)
      for neighbor in graph[current]:
        if neighbor not in visited:
          stack.append(neighbor)
    groups.append(group)
  return groups

def get_true_frequencies(frequencies, name_pairs):
  groups = get_name_groups(name_pairs)
  canonical = {}
  for group in groups:
    for i in xrange(1, len(group)):
      canonical[group[i]] = group[0]
  true_frequencies = collections.defaultdict(int)
  for name in frequencies:
    if name in canonical:
      true_frequencies[canonical[name]] += frequencies[name]
    else:
      true_frequencies[name] += frequencies[name]  # =?
  return true_frequencies

# Test
# abcd, efg
name_pairs = [("a", "b"), ("c", "d"), ("a", "c"), ("e", "f"), ("f", "g")]
frequencies = {"a": 10, "b": 20, "c": 30, "d": 40, "e": 50, "f": 60, "g": 70, "h": 80}
print get_name_groups(name_pairs)
print "abcd, efg"
print get_true_frequencies(frequencies, name_pairs)
print "abcd: 100, efg: 180, h: 80"

# Time: 23 minutes

###
# Mistakes / Bugs / Misses
###
# Didn't think of one-off question until testing
# Missed that they had an example input, would have used that as a test.
# Thought about but did not mention the merging solution, which is a bit worse.

