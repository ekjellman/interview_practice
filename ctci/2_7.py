import linked_list

###
# Problem
###

# Determine if two singly linked lists intersect

###
# Work
###

# Can't think of any questions. Most questions I'd ask (input/output types)
# are specified. I could ask some questions about use cases or how this would
# be used in practice, but this is basically a canonical testing question.
# I'd still come up with a few questions to ask in an interview, though.

def get_length(ll):
  length = 0
  current = ll.head
  while current is not None:
    length += 1
    current = current.next
  return length

def advance(node, n):
  # TODO error checking
  current = node
  while n > 0:
    n -= 1
    current = current.next
  return current

def intersects(a, b):
  a_length = get_length(a)
  b_length = get_length(b)
  a_current = a.head
  b_current = b.head
  if a_length > b_length:
    a_current = advance(a_current, a.length - b.length)
  if a_length < b_length:
    b_current = advance(b_current, b.length - a.length)
  while a_current is not None:
    if a_current == b_current:
      return a_current
    a_current = a_current.next # Or use advance
    b_current = b_current.next
  return None

a = linked_list.LinkedList()
a.add(1)
a.add(2)
a.add(3)
a.add(4)
a.add(5)
b = linked_list.LinkedList()
b.add(1)
b.add(2)
b.add(3)
b.add(4)
b.add(5)
print "None", intersects(a, b)

a = linked_list.LinkedList()
a.add(1)
a.add(2)
a.add(3)
a.add(4)
a.add(5)
b = linked_list.LinkedList()
b.add(6)
b.add(7)
join_node = a.find(3)
b_node = b.find(7)
b_node.next = join_node
print "node", intersects(a, b)

# Time: 10 minutes

###
# Mistakes / Bugs / Misses
###
# At 39 and 41, I used a.length instead of a_length (same with b)
# Before adding the second test case, I returned True/False instead of
#   node / None
# Did not think to compare tails of list. That's interesting because it means
#   that there certainly IS a collision, which makes the code more compact.
# I like her approach for finding the longer list and putting it in a variable
#   better than my approach

