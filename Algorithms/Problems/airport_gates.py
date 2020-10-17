"""
Airport gates - from Peak6

"""

#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getMinGates' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY landingTimes
#  2. INTEGER_ARRAY takeOffTimes
#  3. INTEGER maxWaitTime
#  4. INTEGER initialPlanes
#

def addTime(curr_time, time):
    curr_time += time
    if curr_time % 100 > 60:
        curr_time += 100 - 60
    return curr_time

def getMinGates(landingTimes, takeOffTimes, maxWaitTime, initialPlanes):

    # init values
    curr_gates, max_gates = initialPlanes, initialPlanes
    curr_time = landingTimes[0] if landingTimes else 0

    # Try to land all planes and bring them to gate
    takeoff_ptr = 0
    for plane_landing in landingTimes:
        # Increment time by max wait time
        curr_time = addTime(plane_landing, maxWaitTime)
        print(curr_time, curr_gates, takeoff_ptr)

        # Take off eligible planes
        while curr_gates >= 1 and takeoff_ptr < len(takeOffTimes) and curr_time >= takeOffTimes[takeoff_ptr]:
            takeoff_ptr += 1
            curr_gates -= 1

        # Bring waiting plane to gate
        curr_gates += 1

        # Update max gates
        max_gates = max(max_gates, curr_gates)

    return max_gates




if __name__ == '__main__':
