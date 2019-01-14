###
# Problem
###

# Find the number of ways to parenthesize a boolean expression to make it
# evaluate a certain way. For example, 1^0|0|1 -> False in two ways
#
# 1^(0|(0|1)
# 1^((0|0)|1)

###
# Work
###

# Questions:
# Input type? (Assume string)
# Input valid? (Assume yes)
# Expected size of string

def ways(expression, result):
  print expression
  if len(expression) == 1:   # Single 0 or 1
    return 1 if (expression == "1") == result else 0
  count = 0
  for op_pos in xrange(1, len(expression), 2):
    pre = expression[:op_pos-1]
    post = expression[op_pos+2:]
    current = expression[op_pos-1:op_pos+2]
    evaluation = eval_expression(current)
    count += ways(pre+evaluation+post, result)
  return count

def eval_expression(expr):
  # Could use eval(), but unsafe?
  assert len(expr) == 3
  assert expr[0] in ("01")
  assert expr[2] in ("01")
  assert expr[1] in ("&|^")
  a = expr[0] == "1"
  b = expr[2] == "1"
  if expr[1] == "&":
    result = a & b
  elif expr[1] == "|":
    result = a | b
  else:
    result = a ^ b
  return "1" if result else "0"

#print "2", ways("1^0|0|1", False)
print "10", ways("0&0&0&1^1", True)
#print "1", ways("1", True)
#print "0", ways("0", True)

# Time: 25 minutes. FAILED
# Study this problem, and make a card for catalan numbers, lol

###
# Mistakes / Bugs / Misses
###
# Apparently miscounted results. Come back and study this one more.
# Minor typos even up to that point.
