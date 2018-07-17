import linked_list

###
# Problem
###

# Partition a linked list around a given value, so that all nodes greater than
# that value come after all nodes less than that value.

###
# Work
###

# Questions:
# -- Return nothing? (Assume yes)
# -- Input is head of the list? (Assume yes)

# Possible approaches:
# -- Punt all greater values to the end, but then infinite loop problems
# -- Two linked lists, then join them, but additional space.
#   -- Can remove from the linked list as we process. O(1) space
#   -- Can also just have one extra linked list for the greater values.

def partition(ll, partition_value):
  greater_values = linked_list.LinkedList()
  current = ll.head
  while current is not None:
    if current.value >= partition_value and current.next is not None:
      # Remove node
      greater_values.add(current.value)
      current.value = current.next.value
      current.next = current.next.next
    else:
      current = current.next
  greater_node = greater_values.head
  while greater_node is not None:
    ll.add(greater_node.value)
    greater_node = greater_node.next

test_list = linked_list.LinkedList()
test_list.add(9)
test_list.add(1)
test_list.add(8)
test_list.add(2)
test_list.add(3)
test_list.add(7)
test_list.add(6)
test_list.add(4)
test_list.add(0)
test_list.add(10)
test_list.print_list()
partition(test_list, 5)
test_list.print_list()

# Time: 14 minutes

###
# Mistakes / Bugs / Misses
###

# Original version went to current.next when I removed a node, sometimes
# skipping nodes that I needed to put on greater_values
