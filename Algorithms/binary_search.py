# Pseudocode
"""
    Procedure binary_search
        A ← sorted array
        n ← size of array
        x ← value to be searched

        Set lowerBound = 1
        Set upperBound = n

        while x not found
            if upperBound < lowerBound
                EXIT: x does not exists.

            set midPoint = lowerBound + ( upperBound - lowerBound ) / 2
            if A[midPoint] < x
                set lowerBound = midPoint + 1
            if A[midPoint] > x
                set upperBound = midPoint - 1
            if A[midPoint] = x
                EXIT: x found at location midPoint
        end while
    end procedure
"""

# Recursive binary search.
# Returns index of x in arr if present, else -1
def binary_search(arr, low, high, x):

    # Check base case
    if high < low:
        # Element is not present in the array
        return -1

    # CHECK mid and recurse on either side
    mid = (high + low) // 2

    # If element is present at the middle itself
    if arr[mid] == x:
        return mid

    # If element is smaller than mid, then it can only
    # be present in left subarray
    elif arr[mid] > x:
        return binary_search(arr, low, mid - 1, x)

    # Else the element can only be present in right subarray
    else:
        return binary_search(arr, mid + 1, high, x)



# Test array
arr = [ 2, 3, 4, 10, 40 ]
x = 10

# Function call
result = binary_search(arr, 0, len(arr)-1, x)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")

################################################

# Iterative Binary Search Function
# It returns index of x in given array arr if present,
# else returns -1
def binary_search_2(arr, x):
	low = 0
	high = len(arr) - 1
	mid = 0

	while low <= high:

		mid = (high + low) // 2

		# Check if x is present at mid
        if arr[mid] == x:
            return mid

		# If x is greater, ignore left half
        elif arr[mid] < x:
			low = mid + 1

		# If x is smaller, ignore right half
		elif arr[mid] > x:
			high = mid - 1


	# If we reach here, then the element was not present
	return -1


# Test array
arr = [ 2, 3, 4, 10, 40 ]
x = 10

# Function call
result = binary_search_2(arr, x)

if result != -1:
	print("Element is present at index", str(result))
else:
	print("Element is not present in array")
