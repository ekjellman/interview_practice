###
# Problem
###

# You have a class with three methods, first() second() and third().
# Thread A calls first(), Thread B calls second(), Thread C calls third()
# Design a mechanism that insures first is called before second is called before
# third

###
# Work
###

# Questions:
# Do we have access to change the Foo class? (assume no)
# Use cases
# What should we do if we try to access out of order? Block? Return false?
#   raise an error?
# Can first/second/third be called multiple times, or once and only once?

# If we don't have the ability to change the Foo class itself, we can make
# a wrapper around Foo and pass it to our three threads. This wrapper will
# construct the actual Foo object and store it as a member variable. Then,
# the threads will call members of the FooWrapper. There, we'll have a variable
# that indicates which functions can be called, and if the appropriate functions
# haven't been called yet, do whatever it says. We'd also probably want a lock
# object on the FooWrapper.

# Something like this:

"""
class FooWrapper(object):
  def __init__(self):
    self.foo = Foo()
    self.callable = 1

  def first():
    foo.first()
    self.callable = 2

  def second():
    if self.callable < 2:
      # do something
      # return?
    foo.second()
    self.callable = 3

  def third()
    if self.callable < 3:
      # do something / return
    foo.third()
"""

# Time: 12 minutes

###
# Mistakes / Bugs / Misses
###
# It seems like they did a similar thing with semaphores.
# TODO: Do I need to do a similar thing in Python? (Lock / Semaphore / Reentrant
#       Lock)

