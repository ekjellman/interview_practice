###
# Problem
###

# Write a method to return all the subsets of a set

# Questions:
# Size of the set?
# Can we assume the set doesn't have duplicates?

###
# Work
###

# There's a more straightforward recursive solution, but I feel like writing
# something a bit different for practice.

def subsets(input_set):
  input_list = list(input_set)  # Can't index into a set
  for i in xrange(2**len(input_list)):
    output_set = set()
    for item_number in xrange(len(input_list)):
      if (1 << item_number) & i != 0:
        output_set.add(input_list[item_number])
    yield output_set

# Test
for output in subsets(set((1, 2, 3, 4, 5))):
  print output

# Time: 5 minutes

###
# Mistakes / Bugs / Misses
###
# It could be me, but I think this solution is a little harder to read and
# understand than the recursive solution, so I'd want to talk through that
# with an interviewer. I would also want to mention other solutions, and not
# jump into this one without checking first.

# In Python, I also think it's a better solution to implement this as a
# generator, instead of returning all subsets from one call.

