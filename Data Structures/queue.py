### Python implementation of Queue

# List implementation (not optimal)
# List is represented internally as an array

class Queue:

  def __init__(self):
    self.queue = []

  # enqueue is to append to the tail of the list - O(1)
  def enqueue(self, element):
    self.queue.append(element)
    return self.queue

  # dequeue is to remove from the head of the list - O(n)
  def dequeue(self):
    return self.queue.pop(0)

  def checkHead(self):
    return self.queue[0]

  def checkTail(self):
    return self.queue[-1]

#######################################################

# Deque implementation (optimal)
# Deque = doubly-ended queue
# Represented internally as a doubly-linked list

import collections # has deque

# initializing deque
de = collections.deque([1,2,3])

# 1) Add to right and remove from left - O(1)
de.append(4)
de.popleft()

# 2) Add to left and remove from right - O(1)
de.appendleft(4)
de.pop()
