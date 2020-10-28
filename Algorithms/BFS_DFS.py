"""BFS, DFS"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""
Breadth-First Search with a Queue:

    explore by steps (find all possible next valus and enqueue them)
    Create a set (has been visited)
    Create a Queue (will be visited)
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
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: # Base case
            return []

        traversal = []
        zig_reverse = False # Flag for direction of zigzag

        # Breadth-first traversal
        level = [root]
        while level:
            # Get list of values in level
            level_vals = []
            for node in level:
                level_vals.append(node.val)

            # Append level order to traversal, flipping direction
            traversal.append(level_vals[::-1]) if zig_reverse else traversal.append(level_vals)
            zig_reverse = not zig_reverse

            next_level = []
            # Add each child node to next_level
            for node in level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            level = next_level

        return traversal
        

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
"""

"""
Depth-First Search with Recursion:
"""

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        level_order = []
        def traverse(node, depth):
            if node:
                if depth >= len(level_order): # we are at a new level
                    level_order.append([node.val])
                else:
                    if depth & 1:
                        level_order[depth].insert(0, node.val)
                    else:
                        level_order[depth].append(node.val)
                traverse(node.left, depth+1)
                traverse(node.right, depth+1)

        traverse(root, 0)
        return level_order
