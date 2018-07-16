class Node(object):
  def __init__(self, value):
    self.value = value
    self.next = None

class LinkedList(object):
  # Implement a simple singly-linked list for use in CTCI problems
  def __init__(self):
    self.head = None
    self.tail = None

  def add(self, value):
    node = Node(value)
    if self.tail is None:
      self.tail = node
    else:
      node.previous = self.tail
      self.tail.next = node
      self.tail = node
    if self.head is None:
      self.head = node

  def find(self, value):
    current = self.head
    while current is not None:
      if current.value == value: return current
      current = current.next
    return None

  def print_list(self):
    print "[",
    current = self.head
    while current is not None:
      print current.value,
      current = current.next
    print "]"

if __name__ == "__main__":
  a = LinkedList()
  a.add(1)
  a.add(2)
  a.add(3)
  a.add(4)
  a.print_list()
  node = a.find(3)
  print node
  print node.value
  print node.next
  print node.next.value

