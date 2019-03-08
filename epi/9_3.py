###
# Problem
###

# Test a string for well formedness over {} [] ()

###
# Work
###
# Questions:
# Only those 6 characters? (assume yes)
# Length of string

def well_formed(s):
  stack = []
  for c in s:
    if c in "[{(":
      stack.append(c)
    elif c in "]})":
      if not stack: return False
      match = stack.pop()
      if c == "]" and match != "[": return False
      if c == ")" and match != "(": return False
      if c == "}" and match != "{": return False
  return len(stack) == 0

# Tests
print well_formed("[{()}]"), True
print well_formed(""), True
print well_formed("[{()]}"), False
print well_formed("[{(}]"), False
print well_formed("[{()}"), False
print well_formed("[](){}[[[]]][({})]"), True
print well_formed("([]){()}"), True
print well_formed("[()[]{()()}]"), True
print well_formed("[)"), False
print well_formed("[()[]{()()"), False
print well_formed("]"), False

# Time: 6 minutes

###
# Mistakes / Bugs / Misses
###
# Didn't check if stack was empty when popping until reading answer.
