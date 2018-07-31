###
# Problem
###

# Explain the data structures and algorithms you would use to design an
# in-memory file system.

###
# Work
###
# Questions:
# Do we want a way to write this out to disk?
# Number of files? Type of file system?
# Do we need to handle permissions and things like that?
# Are we handling RAM allocation, things like that?
# symlinks?

# This problem is kind of huge >_< It's unclear to me what she means by
# in-memory, I'm hoping it is a way to avoid dealing with disk sectors and
# such.

# Anyway, we can think of a tree. A FileObject is the parent class and holds
# generic information both Files and Folders need.

class FileObject(object):
  pass
  # name
  # created date
  # permissions
  # etc

# Then we can have a File object, which we can think of as the leaf of a tree.

class File(FileObject):
  pass
  # actual file byte data

# And a folder object, which holds other FileObjects (either Files or Folders)
class Folder(FileObject):
  pass
  # List of FileObjects

# This is a starting point, and I just feel like I need more info from the
# interviewer to proceed from here. I'll see what big ideas I missed.

# Time: 8 minutes

###
# Mistakes / Bugs / Misses
###
# Did not discuss useful file methods (like delete, touch, create, list, etc)

