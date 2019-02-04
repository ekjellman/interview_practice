###
# Problem
###

# XML is verbose. You're given a way of encoding XML where each tag gets mapped
# to an int.
# Given a passed in Element object (and its children) output the encoded XML

###
# Work
###
# Questions:
# Input? (Assuming an Element object and a dictionary mapping)
# Output? (Assuming a string of the mapping)
# Possible output size? (Assume relatively small. We'll stick with passing
#   strings around, but it might be better to pass a list of tokens and join
#   them at the end)
# Are we going to need to go the other way at some point? (Assume no)
# (found in test) The encoding isn't complete. How do you have a value for an
#   Element? i.e. the "Some Message" part. (I guess it's just a child)

# TODO: All kinds of error checking
END_VALUE = "0"

class Element(object):
  def __init__(self, tag, attributes, children):
    self.tag = tag
    self.attributes = attributes
    self.children = children

  def encoding(self, mapping):
    assert self.tag in mapping
    parts = []
    parts.append(str(mapping[self.tag]))
    for attribute in self.attributes:
      parts.append(attribute.encoding(mapping))
    parts.append(END_VALUE)
    for child in self.children:
      if type(child) is Element:
        parts.append(child.encoding(mapping))
      else:
        parts.append(child)
    parts.append(END_VALUE)
    return " ".join(parts)

class Attribute(object):
  def __init__(self, tag, value):
    self.tag = tag
    self.value = value

  def encoding(self, mapping):
    parts = []
    parts.append(str(mapping[self.tag]))
    parts.append(self.value)
    return " ".join(parts)

# Test
mapping = {"family": 1, "person": 2, "firstName": 3, "lastName": 4, "state": 5}
first_name = Attribute("firstName", "Gayle")
person = Element("person", [first_name], ["Some Message"])
last_name = Attribute("lastName", "McDowell")
state = Attribute("state", "CA")
family = Element("family", [last_name, state], [person])

print family.encoding(mapping)

# Time: 20 minutes

###
# Mistakes / Bugs / Misses
###
# Forgot self in lines 35 and 38
# Forgot str at lines 34 and 53
