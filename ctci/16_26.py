###
# Problem
###

# Given an arithmetic equation consisting of positive integers + - * / and
# no parens, compute the result.

###
# Work
###
# Questions:
# Follow MDAS order? (Assume yes)
# Allow non-integer results? (Assume yes)
#   -- Get exact answers? (Assume no)
# What to do with invalid operations? (Primarily div zero) (assume raising error
#   is fine)
# What to do with invalid expressions? (Raising error is fine)
# Use eval? (Assume no)

import collections

def calc(equation):
  tokens = tokenize_equation(equation)
  for ops in ("*/", "+-"):
    tokens = handle_ops(tokens, ops)
  assert len(tokens) == 1
  return tokens[0]

def tokenize_equation(equation):
  # TODO: Error checking
  tokens = collections.deque()
  current_num = ""
  for char in equation:
    if char in "0123456789":
      current_num += char
    elif char in "*+/-":
      number = int(current_num)   # Raises
      current_num = ""
      tokens.append(number)
      tokens.append(char)
    else:
      raise ValueError("Invalid Character")
  number = int(current_num)   # Raises
  tokens.append(number)
  return tokens

def handle_ops(tokens, ops):
  # TODO: Replace assertions with error checking
  for op in ops:
    assert op in "*/+-"
  new_tokens = collections.deque()
  while len(tokens) > 1:
    a = tokens.popleft()
    op_token = tokens.popleft()
    b = tokens.popleft()
    if op_token in ops:
      if op_token == "*":
        result = a * b
      elif op_token == "/":
        result = a / float(b)
      elif op_token == "+":
        result = a + b
      elif op_token == "-":
        result = a - b
      else:
        raise ValueError("Invalid expression")
      tokens.appendleft(result)
    else:
      new_tokens.append(a)
      new_tokens.append(op_token)
      tokens.appendleft(b)
  assert len(tokens) == 1
  new_tokens.append(tokens[0])
  return new_tokens

# Tests:
print calc("2*3+5/6*3+15"), 23.5
print calc("6-5-2"), -1
# Tests about error conditions:
# -- op at beginning of string
# -- two ops in a row
# -- empty string
# -- Div zero (and more complicated div zero like 3*0/3*0)
# -- non-number and op characters (like spaces, etc)

# Time: 28 minutes (I gave myself more than 25, because one of the assumptions
#       I listed led to a different answer than she gave, see below. I finished
#       the original version in 21 minutes)

###
# Mistakes / Bugs / Misses
###
# Not sure how to split on multiple things
# Make cards about common errors (ValueError etc)
# Had a copy/paste error in + and - ops
# Forgot to reset current_num when we found an op
# Had op instead of op_token in handle_ops
# My original version gave a different result than Gayle's, since I handled
#   one op at a time, instead of groups of two ops. So I did * first, then /,
#   etc.. Afterwards I changed it to the above.
# Did not think about the stack solution. TODO
