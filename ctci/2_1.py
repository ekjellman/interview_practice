import linked_list

###
# Problem
###

# Remove duplicate values from an unsorted linked list
# Follow up: What if you can't use a temporary buffer?

###
# Work
###

# Questions:
# Singly or doubly linked list? (Assuming singly)
# Note: Not solving with recursion
# Return value? (Assume none, although number of nodes removed is possible.)

def remove_duplicates(ll):
  values = set()
  current = ll.head
  previous = None
  while current is not None:
    if current.value in values:  # Can't happen for head
      # Delete node
      previous.next = current.next
      current = current.next
    else:
      values.add(current.value)
      previous = current
      current = current.next

test_list = linked_list.LinkedList()
test_list.add(1)
test_list.add(2)
test_list.add(3)
test_list.add(4)
test_list.add(2)
test_list.add(3)
test_list.add(4)
test_list.add(2)
test_list.add(3)
test_list.add(5)
test_list.print_list()
remove_duplicates(test_list)
test_list.print_list()

def remove_duplicates_no_space(ll):
  value_node = ll.head
  while value_node is not None:
    current = value_node.next
    previous = value_node
    while current is not None:
      if current.value == value_node.value:
        # Delete node
        previous.next = current.next
        current = current.next
      else:
        previous = current
        current = current.next
    value_node = value_node.next

test_list = linked_list.LinkedList()
test_list.add(1)
test_list.add(2)
test_list.add(3)
test_list.add(4)
test_list.add(2)
test_list.add(3)
test_list.add(4)
test_list.add(2)
test_list.add(3)
test_list.add(5)
test_list.print_list()
remove_duplicates_no_space(test_list)
test_list.print_list()

# Time: 13 minutes

###
# Mistakes / Bugs / Misses
###
# -- Did not think about return value until after coding first version
# -- In the no space version, lines 51-52 were initialized incorrectly
#    (Was value_node / None)
