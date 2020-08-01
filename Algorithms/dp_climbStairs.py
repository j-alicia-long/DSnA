# This is a dp problem
# - Optimal substructure (overlapping subproblems)


import collections

class Solution:

    # Iterative solution (timeout)
    # O(2^n) time, O(2^n) space
    def climbStairs1(self, n: int) -> int:

        # Queue objects: (curr_level, num_paths_to_level)
        queue = collections.deque([0])
        total_paths = 0

        while queue:
            # Get next node (step) in traversal queue
            curr_level = queue.popleft(0)

            # Add step if not at end
            for step in [1,2]:
                next_step = curr_level+step
                if next_step == n: # Count when finished
                    total_paths += 1
                elif next_step < n:
                    queue.append(next_step)

        return total_paths


    ###############
    # Top-down Recursive solution
    # O(n) time, O(n) space
    # W/o memoization: O(2^n) time, O(n) space for recursive call stack?
    def climbStairs2(self, n: int) -> int:

        @lru_cache() # memoization
        def countAllSteps(n, curr_level: int) -> int:

            # Base case: check validity
            if curr_level > n:
                return 0
            if curr_level == n:
                return 1

            # Else if more steps remaining, add steps
            return countAllSteps(n, curr_level+1) + countAllSteps(n, curr_level+2)

        return countAllSteps(n, 0)


    ###############
    # Bottom-up iterative solution
    # O(n) time, O(1) space
    def climbStairs3(self, n: int) -> int:

        # Recurrence: f(n) = f(n-1) + f(n-2)
        # one path from f(n-1), two paths from f(n-2)
        # Note - this is fibonacci?

        # Base cases:
        if n < 3:
            return n

        # Generate values 1 to n
        two_below = 1
        one_below = 2
        curr_level = 3

        while curr_level <= n:
            # Calculate paths to current step
            num_paths = one_below + two_below

            # Update pointers
            two_below = one_below
            one_below = num_paths
            curr_level += 1

        return one_below
