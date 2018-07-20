###
# Problem
###

# Given a directed graph, make an algorithm to find if there is a route between
# the two nodes

###
# Work
###

# Questions:
# What format will the graph be in? (Assume "whatever format you want")
# Do the vertices have labels we can use? (Assume yes, strings)

def route_exists(graph, start, end):
  seen = set()
  # Since we don't care about fastest path, DFS or BFS doesn't matter
  stack = []
  stack.append(start)
  seen.add(start)
  while stack:
    current = stack.pop()
    if current not in graph: continue
    for neighbor in graph[current]:
      if neighbor == end: return True
      if neighbor not in seen:
        stack.append(neighbor)
        seen.add(neighbor)
  return False

test_graph = {"A": set("BCDE"),
              "B": set("ACE"),
              "C": set("F"),
              "D": set("A"),
              "E": set("GHI"),
              "F": set("J")}

print route_exists(test_graph, "A", "J")
print route_exists(test_graph, "A", "K")

# Time: 9 minutes

###
# Mistakes / Bugs / Misses
###
# Did not remember if set("STRING") got you a set of the string's letters
# Lines 39-40: Used graph instead of test_graph
# Did not think of "vertex not in the graph" case at line 24
