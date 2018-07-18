import linked_list

###
# Problem
###

# Find the node at the beginning of a loop of a (corrupt) circularly linked list

###
# Work
###

# Questions:
# What will this be used for? Why do we expect this to happen? (Might give us
#   some special knowledge how it can be determined)

# I know that there is a better approach, but after 10 minutes I can't think of
# it or derive it, so I'm going with this somewhat suboptimal approach.
# One worse approach than this is to use a set for nodes (worse in terms of
# space, anyway)

def find_loop_node(ll):
  # Determine if the list is circular
  fast = ll.head
  slow = ll.head
  while fast is not None:
    fast = fast.next
    if fast is not None: fast = fast.next
    slow = slow.next
    if fast == slow:
      meeting_node = fast
      break
  if fast is None:
    return None
  node_set = set()
  while fast not in node_set:
    node_set.add(fast)
    fast = fast.next
  current = ll.head
  while current not in node_set:
    current = current.next
  return current

a = linked_list.LinkedList()
a.add(1)
a.add(2)
a.add(3)
a.add(4)
a.add(5)
a.add(6)
a.add(7)
loop_node = a.find(3)
last_node = a.find(7)
last_node.next = loop_node
result = find_loop_node(a)
print result
if result:
  print result.value

a = linked_list.LinkedList()
a.add(1)
a.add(2)
a.add(3)
a.add(4)
a.add(5)
a.add(6)
a.add(7)
result = find_loop_node(a)
print result
if result:
  print result.value

# Time: 25 minutes (time ran out)

###
# Mistakes / Bugs / Misses
###
# Did not find optimal approach. REDO
# Key missed insight: Once we find the fast/slow collision point, we know
#                     both the collision point and the start of the list are
#                     k nodes from the start of the loop. So we can advance
#                     from both the collision point and the start of the list
#                     until THOSE pointers collide, and it's the start of the
#                     list.
