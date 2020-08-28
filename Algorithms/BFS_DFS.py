"""
Depth-First Search with a Stack:

    go down a path until we get to a dead end, then backtrack
    Create a set (has been visited)
    Create a stack (to be visited)
    Add root to stack
    while the stack is not empty
        Curr = get the top element in stack
        Return true if cur is target
        Iterate through neighbors
            If neighbor has not been visited
                Mark it as visited
                Add it to the stack

    If it gets to here, there is no path so return false


Breadth-First Search with a Queue:
    explore by steps (find all possible next valus and enqueue them)
    Create a Queue (will be visited)
    Create a set (has been visited)
    Keep track of num steps
    Add root to queue
    while queue is not empty
        Increase Steps
        Save queue size cause this will change
        Iterate from 0 to saved queue size
        Curr = get first node from queue
        return step if curr is target
        Find all possible next choices and enqueue them (if not visited yet)

    If it gets to here, there is no path so return false

"""
