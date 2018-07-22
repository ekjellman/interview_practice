###
# Problem
###

# Validate a BST

###
# Work
###
# Questions:
# Input/Output types (Assume bst of ints, returns a boolean)
# Unique items? (Assume yes)
# Empty tree valid? (Assume yes)

class BST(object):
  def __init__(self, value):
    self.value = value
    self.right = None
    self.left = None

def validate_bst(bst, low=float("-inf"), high=float("inf")):
  if not bst:
    return True
  if bst.left:
    if bst.left.value >= bst.value or bst.left.value <= low:
      return False
  if bst.right:
    if bst.right.value <= bst.value or bst.right.value >= high:
      return False
  return (validate_bst(bst.left, low=low, high=bst.value) and
          validate_bst(bst.right, low=bst.value, high=high))

bst = BST(20)
bst.left = BST(10)
bst.right = BST(30)
bst.left.left = BST(5)
bst.left.right = BST(15)
bst.right.left = BST(25)
bst.right.right = BST(35)
print "True", validate_bst(bst)

bst = BST(20)
bst.left = BST(10)
bst.right = BST(30)
bst.left.left = BST(5)
bst.left.right = BST(15)
bst.right.left = BST(19)
bst.right.right = BST(35)
print "False", validate_bst(bst)

bst = BST(20)
bst.left = BST(10)
bst.right = BST(30)
bst.left.left = BST(5)
bst.left.right = BST(21)
bst.right.left = BST(25)
bst.right.right = BST(35)
print "False", validate_bst(bst)
# Time: 11 minutes

###
# Mistakes / Bugs / Misses
###
# Forgot closing paren on line 31
# Did not consider in-order traversal idea
