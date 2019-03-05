class ListNode(object):
  def __init__(self, value):
    self.value = value
    self.next_node = None

  # Convenience methods
  def traversal(self):
    values = []
    current = self
    while current:
      values.append(current.value)
      current = current.next_node
    return values

  def find(self, value):
    current = self
    while current:
      if current.value == value: return current
      current = current.next_node
    return None

  @staticmethod
  def make_list(items):
    current = ListNode(0)
    dummy_head = current
    while items:
      current.next_node = ListNode(items.pop(0))
      current = current.next_node
    return dummy_head.next_node

if __name__ == "__main__":
  ll = ListNode.make_list([1, 2, 3, 4, 5])
  print ll.traversal()


# TODO: 11 was values.append(self.value). Make a card for this bug.
# TODO: make list for staticmethod (had @static_method)
#       classmethod too?
# TODO: Make card for collections.OrderedDict
