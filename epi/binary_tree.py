class BinaryTree(object):
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
    self.subtree_nodes = 0
    self.parent = None
    self.locked = False  # Used for 10.15

  def populate(self):
    if self.left: self.left.populate()
    if self.right: self.right.populate()
    self.subtree_nodes = 1
    if self.left: self.subtree_nodes += self.left.subtree_nodes
    if self.right: self.subtree_nodes += self.right.subtree_nodes

  def make_parents(self):
    if self.left:
      self.left.parent = self
      self.left.make_parents()
    if self.right:
      self.right.parent = self
      self.right.make_parents()

  def in_order(self):
    left_sub = self.left.in_order() if self.left else []
    right_sub = self.right.in_order() if self.right else []
    return left_sub + [self] + right_sub

  def pre_order(self):
    left_sub = self.left.pre_order() if self.left else []
    right_sub = self.right.pre_order() if self.right else []
    return [self] + left_sub + right_sub


# Test
if __name__ == "__main__":
  a = BinaryTree(10)
  b = BinaryTree(5)
  c = BinaryTree(15)
  d = BinaryTree(3)
  e = BinaryTree(7)
  f = BinaryTree(12)
  g = BinaryTree(17)

  a.left = b
  a.right = c
  b.left = d
  b.right = e
  c.left = f
  c.right = g
  a.populate()
  print a.subtree_nodes
  print c.subtree_nodes
  print e.subtree_nodes

  a.make_parents()
  for node in (a, b, c, d, e, f, g):
    print node.value, node.parent.value if node.parent else None

  for node in a.pre_order():
    print node.value,
  print

  for node in a.in_order():
    print node.value,
  print
