###
# Problem
###

# Determine whether the string representation of an integer is a palindrome

###
# Work
###
# Questions:
# How long is the number? (Because I'm gonna use O(n) space, probably)

# Ok, so my answer to this really is going to depend on how much of a jerk
# the interviewer is. My real answer looks something like:

def is_palindrome(n):
  return str(n) == str(n)[::-1]

# Tests:
print "All True:"
print is_palindrome(0)
print is_palindrome(1)
print is_palindrome(7)
print is_palindrome(11)
print is_palindrome(121)
print is_palindrome(333)
print is_palindrome(2147447412)
print "All False:"
print is_palindrome(-1)
print is_palindrome(12)
print is_palindrome(100)
print is_palindrome(2147483647)

# It could be that the interviewer will not allow me to use str() or check
# reverse with [::-1]. In which case:

def is_palindrome_filled_with_hate(n):
  numbers = []
  if n < 0: return False  # always has a -
  while n > 0:  # Could be a function
    next_digit = n % 10
    n /= 10
    numbers.append(next_digit)
  for i in xrange(len(numbers)):  # Could go to /2, could be a function
    if numbers[i] != numbers[-(i+1)]: return False
  return True

# Tests:
print "All True:"
print is_palindrome(0)
print is_palindrome(1)
print is_palindrome(7)
print is_palindrome(11)
print is_palindrome(121)
print is_palindrome(333)
print is_palindrome(2147447412)
print "All False:"
print is_palindrome(-1)
print is_palindrome(12)
print is_palindrome(100)
print is_palindrome(2147483647)

# Time: 9 minutes

###
# Mistakes / Bugs / Misses
###
# Make a card about the reverse of a string in Python. I'm not sure how it
# interacts with .reverse() or reversed() (TODO)
# They made a solution that directly compares the first and last digit by using
# exponentiation. While I should remember this approach (TODO: card), I question
# making the code that much harder to avoid an O(n) space problem. Oh wait it's
# actually O(1) space in Java, because an int is fixed length.
