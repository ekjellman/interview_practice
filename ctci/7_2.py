###
# Problem
###

# Implement a call center with three levels of employees: respondent, manager,
# director. A call must first go to a respondent. If that person cannot handle
# the call, it goes to a manager. If there is no manager or they can't handle
# it, the call goes to a director. Implement dispatchCall()

###
# Work
###
# Questions:
# Is this setup enough, or are we going to want to make it more general?
# (i.e. different call skills, call queues, etc) (assume no for now)
# If there are no respondents available for an incoming call, does it queue,
# or go to an available manager or director? (assume it queues)

# We'll start with the Employee objects. We could either have a generic employee
# object with some object variable indicating level, or we could have different
# classes for the different levels. In a more general system I would go with
# the former, since we'd want to be able to dynamically create new skills or
# levels for the employee. In a less generic system I'd be inclined towards the
# latter. It also matters if, say, a director has other abilities (methods) that
# the employee or manager does not have. If all we're worrying about is
# dispatch_call(), this is less of a concern.

# Let's go for the subclassing employee idea here.

class Employee(object):
  def __init__(self, ...): pass
  def receive_call(self, call): pass  # store current call
  def escalate_call(self): pass  # Gives the call back to the call center
  def complete_call(self): pass  # mark call as complete, get rid of it.

class Respondent(Employee): pass

class Manager(Employee): pass

class Director(Employee): pass

# We also need a call object to pass around and work on.
class Call(object):
  def __init__(self, ...): pass  # store call data like phone number, queue, etc
                                 # Also stores current escalation level
  def complete_call(self): pass  # marks call as completed, does other wrapup

# Now on to the call center.

class CallCenter(object):
  def __init__(self, ...): pass  # Sets up a call queue, or more likely several
                                 # one for each skill / escalation level
                                 # Also sets up Employee queues, one for each
                                 # skill / escalation level. We probably want
                                 # calls to be handed out "fairly"
  def receive_call(self, call): pass  # Put the call into the appropriate queue.
                                      # Employee.escalate_call() would also call
                                      # this for an escalation
  def dispatch_call(self): pass  # This would probably be called repeatedly from
                                 # some other thread to dispatch calls as
                                 # quickly as possible

# dispatch_call would try to match employees with calls, starting from the
# lowest escalation level to the highest. This is because we want to give
# managers "first shot" at handling level two calls.

# Time: 15 minutes (time limit for OO problems)

###
# Mistakes / Bugs / Misses
###
# Study UML?
# She notes that Employee would contain other things not related to the call
# queues specifically. I should have discussed that. It may or may not be that
# those things are outside the scope of call handling.
# Her call object has a lot more stuff. Interesting ones: reply() as a message
# to a call, get/set rank, increment_rank
# I did not note Employee as an abstract class, which it clearly is.



