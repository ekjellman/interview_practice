import collections

###
# Problem
###

# Implement a FIFO data structure for an animal shelter. Animals must be
# adopted in the order they're received (i.e. you get the "oldest" one), but you
# may choose a cat or dog if you wish.

###
# Work
###

# Questions:
# How many animals are we likely to be holding here?
# -- If it's hundreds at most, it might not be worth the effort to avoid some
#    "expensive" min() calls

class Animal(object):
  def __init__(self, admit_time):
    self.admit_time = admit_time
    # TODO: other identifying things

class Dog(Animal):
  pass

class Cat(Animal):
  pass

class AnimalShelter(object):
  def __init__(self):
    self.cat_queue = collections.deque()
    self.dog_queue = collections.deque()

  def enqueue(self, animal):
    # Assumes animals will be enqueued in time order
    if type(animal) is Cat:  # ?
      self.cat_queue.append(animal)
    elif type(animal) is Dog:
      self.dog_queue.append(animal)
    else:
      raise ValueError("Unexpected kind of animal brought to shelter.")

  def dequeueAny(self):
    if not self.cat_queue and not self.dog_queue:
      raise ValueError("Cannot dequeueAny if both queues are empty")

    if not self.cat_queue:
      return self.dequeueDog()
    if not self.dog_queue:
      return self.dequeueCat()

    if self.cat_queue[0].admit_time <= self.dog_queue[0].admit_time:
      # Tiebreak goes to cats, because everyone likes cats more anyway
      return self.dequeueCat()
    else:
      return self.dequeueDog()

  def dequeueCat(self):
    if not self.cat_queue:
      raise ValueError("Cannot dequeueCat if cat queue is empty")
    return self.cat_queue.popleft()

  def dequeueDog(self):
    if not self.dog_queue:
      raise ValueError("Cannot dequeueDog if dog queue is empty")
    return self.dog_queue.popleft()

a = AnimalShelter()
a.enqueue(Cat(1))
a.enqueue(Dog(2))
a.enqueue(Dog(3))
a.enqueue(Cat(4))
a.enqueue(Cat(5))

animal = a.dequeueAny()
print "Cat", animal
print "1", animal.admit_time
animal = a.dequeueDog()
print "Dog", animal
print "2", animal.admit_time
animal = a.dequeueCat()
print "Cat", animal
print "4", animal.admit_time
animal = a.dequeueAny()
print "Dog", animal
print "3", animal.admit_time
print "expect error"
animal = a.dequeueDog()


# Time: 24 minutes (>_<)

###
# Mistakes / Bugs / Misses
###
# Line 52: Missed closing paren
