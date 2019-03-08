###
# Problem
###

# Given a pathname, normalize it.
# Ex: /usr/lib/../bin/gcc  -> /usr/bin/gcc
# Ex: scripts//./../scripts/awkscripts/././ -> scripts/awkscripts

###
# Work
###
# Questions:
# // does nothing? (Assume yes.)
# . stays, .. goes up one? (Assume yes)
# .. at root does nothing? (Assume yes)
# Deal with ~? (Assume no)

def normalize_pathname(s):
  absolute = s[0] == "/"
  tokens = s[1:].split("/")
  stack = []
  for token in tokens:
    if token == "": continue
    elif token == ".": continue
    elif token == "..":
      if not stack: continue
      stack.pop()
    else:
      stack.append(token)
  prefix = "/" if absolute else ""
  return prefix + "/".join(stack)

# Tests:
print normalize_pathname("/usr/lib/../bin/gcc"), "/usr/bin/gcc"
print normalize_pathname("scripts//./../scripts/awkscripts/./."), "scripts/awkscripts"
print normalize_pathname("//./../.././..////"), "/"
print normalize_pathname("//./../.././..////foo/bar/../"), "/foo"

# Time: 7 minutes

###
# Mistakes / Bugs / Misses
###
# Didn't remember that // in the middle of a pathname did nothing?
# Didn't remember what .. did at root  (TODO: Make cards for these two)

