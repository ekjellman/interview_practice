import collections
###
# Problem
###

# Given a list of projects and dependencies, output a build order.

###
# Work
###
# Questions:
# If there are multiple possible build orders, any is ok?

def build_order(projects, dependencies):
  # Implement topological search
  in_degree = {project: 0 for project in projects}
  out_edges = collections.defaultdict(list)
  for dependency in dependencies:
    i, o = dependency
    in_degree[i] += 1
    out_edges[o].append(i)
  build_order = []
  buildable = [project for project in in_degree if in_degree[project] == 0]
  while buildable:
    next_project = buildable.pop()
    build_order.append(next_project)
    for out_edge in out_edges[next_project]:
      in_degree[out_edge] -= 1
      if in_degree[out_edge] == 0:
        buildable.append(out_edge)
  if len(build_order) == len(projects):
    return build_order
  return None  # Should be raise a ValueError

print build_order(["a", "b", "c", "d", "e", "f"],
                  [("d", "a"), ("b", "f"), ("d", "b"), ("a", "f"), ("c", "d")])
print build_order(["a", "b", "c"], [("a", "b"), ("b", "c"), ("c", "a")])

# Time: 11 minutes

###
# Mistakes / Bugs / Misses
###
# variable names are pretty messy
