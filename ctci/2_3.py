import linked_list

###
# Problem
###

# Delete a node in the middle of a singly-linked list, given only access to
# that node

###
# Work
###

# Questions:
# Clarify that we mean delete the value, not the node itself. (Assume yes)
# -- I think deleting the node would require access to head as well, and then
#    be O(n)
# By "middle" this means we won't be removing a node from the end? (Assume yes)

def delete_value(node):
  node.value = node.next.value
  node.next = node.next.next

test_list = linked_list.LinkedList()
test_list.add(1)
test_list.add(2)
test_list.add(3)
test_list.add(4)
test_list.add(5)
test_list.print_list()
node = test_list.find(3)
delete_value(node)
test_list.print_list()
node = test_list.find(1)
delete_value(node)
test_list.print_list()

# Time: 6 minutes

###
# Mistakes / Bugs / Misses
###

# -- Did not add error checking for edge case.
#   -- Note: Book says "nothing is returned", but then returns true/false
#   -- I did ask the "middle" question, but should have thought about returning
#      an error in this case
