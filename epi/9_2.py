###
# Problem
###

# Write a program to evaluate an RPN expression in the form
# "6,4,+,7,2,3,*,9"
# Each RPN expression can be evaluated uniquely to an integer

###
# Work
###
# Questions:
# Integers only? (Assume yes)
# Return type? (Assume integer)
# Errors? Like div 0 or invalid expression (Raising error is ok)

def eval_rpn(s):
  tokens = s.split(",")
  stack = []
  for token in tokens:
    if token in ("*", "/", "+", "-"):
      op_eval(token, stack)
    else:
      stack.append(int(token))
  assert len(stack) == 1
  return stack[0]

def op_eval(token, stack):
  b = stack.pop()
  a = stack.pop()
  if token == "*":
    stack.append(a * b)
  elif token == "/":
    stack.append(a / b)
  elif token == "+":
    stack.append(a + b)
  elif token == "-":
    stack.append(a - b)
  else:
    raise

# Tests:
print eval_rpn("3,4,+,2,*,1,+"), 15
print eval_rpn("1,1,+,-2,*"), -4
print eval_rpn("2,3,4,5,*,*,*"), 120
print eval_rpn("3,6,2,/,/"), 1
print eval_rpn("5,2,-"), 3

# Time: 9 minutes

###
# Mistakes / Bugs / Misses
###

