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

# TODO: 11 was values.append(self.value). Make a card for this bug.
