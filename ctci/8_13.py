###
# Problem
###

# You have a stack of n boxes of given width/height/depth. Boxes cannot be
# rotated. You can only stack a box on top of another box if the box on top is
# smaller in all of height, width, and depth. Compute the height of the tallest
# possible stack.

###
# Work
###

# Questions:
# Can we assume the boxes are sorted in one dimension? (Assume no)
# Expected size of n?
# Type of input? (Assume list of (h, w, d) tuples)
# Can we assume the boxes all have positive dimensions? / Invalid input

def can_stack(current_box, next_box):
  if current_box is None: return True
  return (current_box[0] > next_box[0] and
          current_box[1] > next_box[1] and
          current_box[2] > next_box[2])


def tower_height(boxes, current=None):
  if current is None:
    boxes.sort(reverse=True)  # Sort by height descending
    current_box = None
  elif current == len(boxes):
    return 0
  else:
    current_box = boxes[current]
  best = 0
  for i in xrange(0 if current is None else current + 1, len(boxes)):
    if can_stack(current_box, boxes[i]):
      best = max(best, boxes[i][0] + tower_height(boxes, i))
  return best

boxes = [(25, 25, 25), (20, 20, 20), (15, 15, 15)]
print "60", tower_height(boxes)
boxes = [(25, 25, 25), (20, 40, 20), (15, 15, 60)]
print "25", tower_height(boxes)
boxes = [(40, 25, 25), (50, 40, 20), (65, 15, 60)]
print "65", tower_height(boxes)
boxes = [(23, 40, 40), (25, 35, 45), (5, 37, 39)]
print "28", tower_height(boxes)

# Time: 23 minutes

###
# Mistakes / Bugs / Misses
###
# Spaced out for two minutes thinking about sorting
# I think there might be an interesting graph solution, but I did not reach for
#   it.
# Got xrange wrong at 36 (had xrange(current + 1, len(boxes)), forgetting the
#   None case
# I had a bit of a stumble thinking about how I wanted to pass current along.
#   I eventually did this version which should be more cacheable (although I
#   didn't have time to implement caching in this version.
# ... no caching.
