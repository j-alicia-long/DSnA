### Python implementation of Stack

class Stack:

    # Init stack with empty list
    def __init__(self):
        self.stack = []

    # Append to end of list in O(1)
    def push(self, element):
        self.stack.append(element)
        return self.stack

    # Pop from end of list in O(1)
    def pop(self):
        return self.stack.pop(-1)

    def getTop(self):
        return self.stack[-1]
