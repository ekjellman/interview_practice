###
# Problem
###

# A monochrome screen is stored as a single array of bytes, allowing eight
# consecutive pixels to be stored in one byte. The screen has width w, and
# w is divisible by 8. The height can be derived from the length of the array.
# Implement a function that draws a horizontal line from (x1, y) to (x2, y)

###
# Work
###
# Questions:
# Can we assume valid input? (Assume yes)
# We can modify the screen "array"? (assume yes)

# Note: This makes more sense as a method on a screen object to me, but we will
#       stick to the original question here.

def draw_line(screen, width, x1, x2, y):
  # Brute force
  # TODO error check
  byte_width = width / 8
  y_offset = byte_width * y
  current_byte = x1 / 8 + y_offset
  current_bit = x1 % 8
  byte_end = x2 / 8 + y_offset
  bit_end = (x2 % 8)
  while current_byte != byte_end or current_bit != bit_end:
    screen[current_byte] |= 1 << (7 - current_bit)
    current_bit += 1
    if current_bit == 8:
      current_byte += 1
      current_bit = 0
  screen[current_byte] |= 1 << (7 - current_bit)

def draw_line(screen, width, x1, x2, y):
  # Less brute force
  # TODO error check
  byte_width = width / 8
  y_offset = byte_width * y
  current_byte = x1 / 8 + y_offset
  current_bit = x1 % 8
  byte_end = x2 / 8 + y_offset
  bit_end = (x2 % 8)
  while current_byte != byte_end or current_bit != bit_end:
    if current_byte != byte_end and current_bit == 0:
      screen[current_byte] = 255
      current_byte += 1
    else:
      screen[current_byte] |= 1 << (7 - current_bit)
      current_bit += 1
      if current_bit == 8:
        current_byte += 1
        current_bit = 0
  screen[current_byte] |= 1 << (7 - current_bit)

test_screen = [0] * 16
draw_line(test_screen, 32, 5, 17, 1)
print test_screen
print [0, 0, 0, 0, 7, 255, 192, 0, 0, 0, 0, 0, 0, 0, 0, 0]

test_screen = [0] * 16
draw_line(test_screen, 32, 0, 7, 2)
print test_screen
print [0, 0, 0, 0, 0, 0, 0, 0, 255, 0, 0, 0, 0, 0, 0, 0]

test_screen = [0] * 16
draw_line(test_screen, 32, 24, 31, 3)
print test_screen
print [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255]

test_screen = [0] * 16
draw_line(test_screen, 32, 31, 31, 3)
print test_screen
print [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]

# Time: 22 minutes

###
# Mistakes / Bugs / Misses
###
# Version 1: Had an off by one since I wasn't drawing the last bit
# Did not ask about inclusive/exclusive for x1 x2
# Had a version 3 that had problems with single byte drawing, removed it.
# That version can be written, but the single byte case is tricky. Study it.
